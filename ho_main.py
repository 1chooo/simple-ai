'''
Create Date: 2023/09/01
Author: @1chooo
Version: v0.0.3
'''

import gradio as gr
from Refinaid.Action.ML_configurations import DatasetConfig, DecisionTreeModelConfig, KNNModelConfig
from Refinaid.gui.Utils.Update import update_parameters
from Refinaid.gui.Utils.Update import update_plot_x_parameters
from Refinaid.gui.Utils.Update import update_plot_y_parameters
from Refinaid.gui.Utils.Update import update_model_parameters
from Refinaid.gui.Utils.Update import update_preprocessing_data
from Refinaid.Action.Model import training

demo = gr.Blocks(
    title='Refinaid',
)

dataset_choices = [
    "Titanic", 
    "Diabetes", 
    "House Prices",
]

def _background_listener() -> None:
    dataset_dropdown.change(
        fn=update_parameters,
        inputs=dataset_dropdown,
        outputs=parameters_dropdown,
    )

    dataset_dropdown.change(
        fn=update_plot_x_parameters,
        inputs=dataset_dropdown,
        outputs=x_axis_dropdown,
    )

    dataset_dropdown.change(
        fn=update_plot_y_parameters,
        inputs=dataset_dropdown,
        outputs=y_axis_dropdown,
    )

    model_dropdown.change(
        fn=update_model_parameters,
        inputs=model_dropdown,
        outputs=[
            decision_tree_classifer_title,
            decision_tree_classifer_criterion_dropdown,
            decision_tree_classifer_max_depth_textbox,
            decision_tree_classifer_min_samples_split_slider,
            decision_tree_classifer_min_samples_leaf_slider,
            decision_tree_classifer_max_features_dropdown,
            decision_tree_classifer_max_leaf_nodes_textbox, 
            k_neighbors_classifier_title,
            k_neighbors_classifier_slider,
            k_neighbors_classifier_weights_dropdown,
            k_neighbors_classifier_algorithm_dropdown,
        ]
    )

    submit_dataset_setting_btn.click(
        fn=update_preprocessing_data, 
        inputs=[
            dataset_dropdown, parameters_dropdown, 
            miss_value_checkbox, data_scale_dropdown, 
            training_slider, validation_slider, testing_slider], 
        outputs=[preprocessing_data_result]
    )

    train_btn.click(
        fn=update_training_results,
        inputs=[
            preprocessing_data_result,
            model_dropdown,
            decision_tree_classifer_criterion_dropdown,
            decision_tree_classifer_max_depth_textbox,
            decision_tree_classifer_min_samples_split_slider,
            decision_tree_classifer_min_samples_leaf_slider,
            decision_tree_classifer_max_features_dropdown,
            decision_tree_classifer_max_leaf_nodes_textbox,
            k_neighbors_classifier_slider,
            k_neighbors_classifier_weights_dropdown,
            k_neighbors_classifier_algorithm_dropdown,
        ],
        outputs=[
            training_results,
            train_img1,
            train_img2,
            train_img3,
        ],
    )

def update_training_results(
        preprocessing_data_result,
        model_dropdown,
        decision_tree_classifer_criterion_dropdown,
        decision_tree_classifer_max_depth_textbox,
        decision_tree_classifer_min_samples_split_slider,
        decision_tree_classifer_min_samples_leaf_slider,
        decision_tree_classifer_max_features_dropdown,
        decision_tree_classifer_max_leaf_nodes_textbox, 
        k_neighbors_classifier_slider,
        k_neighbors_classifier_weights_dropdown,
        k_neighbors_classifier_algorithm_dropdown,
        ):
    
    model_config = None
    
    if model_dropdown == "Decision Tree Classifier":
        decision_tree_classifer_max_features_dropdown = decision_tree_classifer_max_features_dropdown if decision_tree_classifer_max_features_dropdown != "None" else None
        model_config = DecisionTreeModelConfig(
            decision_tree_classifer_criterion_dropdown, 
            decision_tree_classifer_min_samples_split_slider, 
            decision_tree_classifer_min_samples_leaf_slider, 
            decision_tree_classifer_max_features_dropdown, 
            eval(decision_tree_classifer_max_depth_textbox), 
            eval(decision_tree_classifer_max_leaf_nodes_textbox),
        )
    elif model_dropdown == "K Neighbor Classifier":
        model_config = KNNModelConfig(
            k_neighbors_classifier_slider, 
            k_neighbors_classifier_weights_dropdown, 
            k_neighbors_classifier_algorithm_dropdown,
        )

    preprocessing_data_value = preprocessing_data_result
    dataset_config=DatasetConfig(
        preprocessing_data_value.loc[0, "Value"],
        preprocessing_data_value.loc[1, "Value"],
        preprocessing_data_value.loc[2, "Value"],
        eval(preprocessing_data_value.loc[3, "Value"]),
        [
            preprocessing_data_value.loc[4, "Value"] / 100,
            preprocessing_data_value.loc[5, "Value"] / 100,
            preprocessing_data_value.loc[6, "Value"] / 100,
        ],
    )

    # TODOs:
    # 這邊已經確定拿得到 model_config, dataset_config
    # 但是後面的 call Refinaid.Action 會出問題
    # 主要需要處理傳入模型，結果顯示 update 我處理好了
    # 但保險起見可能還需再檢查一次
    # 再麻煩 Reeve 了！


    training_outputs = []
    figures, evaluations = training(dataset_config, model_config)
    evaluations = list(map(str,evaluations))

    training_results = gr.DataFrame.update(
        value=[evaluations],
        interactive=True,
    )

    training_outputs.append(training_results)

    train_img1 = gr.Plot(
        interactive=True
    )
    train_img2 = gr.Plot(
        interactive=True
    )
    train_img3 = gr.Plot(
        interactive=True
    )

    img_components = [
        train_img1, 
        train_img2, 
        train_img3
    ]

    for i, component in enumerate(img_components):
        if figures[i] != None:
            training_outputs.append(component.update(value=figures[i], visible=True))
        else:
            training_outputs.append(component.update(visible=False))

    return *training_outputs,


with demo:
    our_heading = gr.Markdown("# Simple AI - Bridging the Gap with AI For Everyone")

    with gr.Tab("Preprocessing"):
        our_heading = gr.Markdown("## Preprocessing")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Dataset")
                dataset_dropdown = gr.Dropdown(
                    label="Select Dataset", 
                    choices=dataset_choices,
                    interactive=True,
                )

                gr.Markdown("### Select Mutiple Parameters")
                parameters_dropdown = gr.Dropdown(
                    label="Select Mutiple Parameters", 
                    choices=[], 
                    interactive=True,
                    multiselect=True,
                )

                gr.Markdown("### Missing Values Handling")
                miss_value_checkbox = gr.Radio(
                    label="Select a Method", 
                    choices=[
                        "Drop Nan", 
                        "By Columns"
                    ], 
                    interactive=True,
                )

                gr.Markdown(f"### Data Scaling")
                data_scale_dropdown = gr.Radio(
                    choices=[
                        "None",
                        "Standard",
                        "Min-Max"
                    ],
                    label="Please select a method",
                    interactive=True,
                )

                gr.Markdown(f"### Data Split\nTotal value should be 100%")

                training_slider = gr.Slider(
                    label="Training Set", 
                    minimum=0, 
                    maximum=100, 
                    step=5,
                    interactive=True,
                )
                validation_slider = gr.Slider(
                    label="Validation Set", 
                    minimum=0, 
                    maximum=100, 
                    step=5,
                    interactive=True,
                )
                testing_slider = gr.Slider(
                    label="Testing Set", 
                    minimum=0, 
                    maximum=100, 
                    step=5,
                    interactive=True,
                )
                submit_dataset_setting_btn = gr.Button(
                    value="Submit Setting",
                )
                
            with gr.Column():
                with gr.Row():
                    gr.ScatterPlot(
                        label="Data Visualization")
                with gr.Row():
                    x_axis_dropdown = gr.Dropdown(
                        label="X Axis", 
                        choices=[], 
                        interactive=True,
                    )
                    y_axis_dropdown = gr.Dropdown(
                        label="Y Axis", 
                        choices=[], 
                        interactive=True,
                    )
        with gr.Row():
            gr.Examples(
                [
                    [
                        "Titanic", 
                        ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"], 
                        "Drop Nan", 
                        "None", 
                        70, 
                        10, 
                        20
                    ],
                    [
                        "Titanic", 
                        ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare"], 
                        "By Columns", 
                        "Standard", 
                        70, 
                        10, 
                        20
                    ],
                    [
                        "Titanic", 
                        ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare"], 
                        "By Columns", 
                        "Min-Max", 
                        70, 
                        10, 
                        20
                    ],
                ],
                [
                    dataset_dropdown,
                    parameters_dropdown,
                    miss_value_checkbox, 
                    data_scale_dropdown, 
                    training_slider, 
                    validation_slider, 
                    testing_slider,
                ]
            )

    with gr.Tab("Training"):
        our_heading = gr.Markdown("## Training")
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Data You have picked!!!")
                preprocessing_data_result = gr.DataFrame(
                    headers=[
                        "Parameters",
                        "Value"
                    ],
                    row_count=(7, "fixed"),
                    col_count=(2, "fixed"),
                    interactive=False,
                )
            with gr.Column():
                model_dropdown = gr.Dropdown(
                    label="Select Model", 
                    choices=[
                        "Decision Tree Classifier", 
                        "K Neighbor Classifier",
                    ], 
                    interactive=True
                )
                # Decision Tree Classifier
                decision_tree_classifer_title = gr.Markdown(
                    "### Decision Tree Classifier", 
                    visible=False,
                )
                decision_tree_classifer_criterion_dropdown = gr.Dropdown(
                    label="Criterion", 
                    choices=[
                        "gini", 
                        "entropy", 
                        "log_loss"
                    ], 
                    value="gini", 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_max_depth_textbox = gr.Textbox(
                    label="Max Depth", 
                    value="None", 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_min_samples_split_slider = gr.Slider(
                    label="Minimum Samples Split", 
                    minimum=2, 
                    maximum=20, 
                    step=1, 
                    value=2, 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_min_samples_leaf_slider = gr.Slider(
                    label="Minimum Samples Leaf", 
                    minimum=1, 
                    maximum=20, 
                    step=1, 
                    value=1, 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_max_features_dropdown = gr.Dropdown(
                    label="Max Features", 
                    choices=[
                        "None", 
                        "sqrt", 
                        "log2"
                    ], 
                    value="None", 
                    interactive=True, 
                    visible=False,
                )
                decision_tree_classifer_max_leaf_nodes_textbox = gr.Textbox(
                    label="Max Leaf Nodes", 
                    value="None", 
                    interactive=True, 
                    visible=False,
                )

                # k_neighbors_classifier
                k_neighbors_classifier_title = gr.Markdown(
                    "### K Neighbors Classifier", 
                    visible=False,
                )
                k_neighbors_classifier_slider = gr.Slider(
                    label="N Neighbors", 
                    value=5, 
                    interactive=True, 
                    minimum=1, 
                    maximum=20, 
                    step=1, 
                    visible=False,
                )
                k_neighbors_classifier_weights_dropdown = gr.Dropdown(
                    label="Weights", 
                    choices=[
                        "uniform", 
                        "distance"
                    ], 
                    value="uniform", 
                    interactive=True, 
                    visible=False,
                )
                k_neighbors_classifier_algorithm_dropdown = gr.Dropdown(
                    label="Algorithm", 
                    choices=[
                        "auto", 
                        "ball_tree", 
                        "kd_tree", 
                        "brute"
                    ], 
                    value="auto", 
                    interactive=True, 
                    visible=False,
                )

        with gr.Row():
            train_btn = gr.Button(
                value="Train"
            )
        with gr.Row():
            gr.Markdown("## Training Result")
        with gr.Row():
            training_results = gr.DataFrame(
                headers=["Accuracy", "Recall", "Precision", "F1"], 
                interactive=True, 
                row_count=(1, "fixed"), 
                col_count=(4, "fixed")
            )

        with gr.Row():
            train_img1 = gr.Plot(
                interactive=True
            )
            train_img2 = gr.Plot(
                interactive=True
            )
            train_img3 = gr.Plot(
                interactive=True
            )

    with gr.Tab("Results"):
        our_heading = gr.Markdown("## Results")
        with gr.Row():
            gr.Textbox("hi")
            gr.Textbox("hi")
        with gr.Row():
            gr.Textbox("hello")
            gr.Textbox("hello")

    _background_listener()

demo.launch(
    # enable_queue=True,
    # share=True, 
    server_name="127.0.0.1", 
    server_port=6006,
    debug=True,
) 
