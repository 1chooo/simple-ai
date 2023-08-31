# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/28
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.1
'''

import gradio as gr
from Refinaid.Action.ML_configurations import DatasetConfig, DecisionTreeModelConfig, KNNModelConfig
from Refinaid.Action.Model import training
from Refinaid.gui.Information import PageContent
from Refinaid.gui.Utils import get_data_setting
from Refinaid.gui.Header import get_header
from Refinaid.gui.Dashborad.Preprocessing import PreprocessingComponent
from Refinaid.gui.Dashborad.Training import TrainingComponent

def build_ui():

    page_content = PageContent()

    model_mapping = {
        "Decision Tree Classifier": "decision_tree_classifier",
        "K Neighbor Classifier": "k_neighbors_classifier",
        "Standard": "standard",
        "Min-Max": "min-max",
        "By Columns": "by_columns",
        "None": None,
        "Drop Nan": None,        
    }

    model_components = {}

    def model_dd_change(model_dd):

        comp_output_list = []
        selected_model = model_mapping[model_dd]
        # print(model_dd)
        # print(selected_model)

        for key in model_components.keys():
            if key not in ["all", "model_selector"]:
                if key == selected_model:
                    for i in range(len(model_components[key])):
                        # print(f"key:{key}\ni:{i}\nitem:{model_components[key][i]}")
                        comp_output_list.append(model_components[key][i].update(visible=True))
                else:
                    for i in range(len(model_components[key])):
                        # print(f"key:{key}\ni:{i}\nitem:{model_components[key][i]}")
                        comp_output_list.append(model_components[key][i].update(visible=False))
        # print(comp_output_list)

        return *comp_output_list,

    def submit_setting_btn_click(dataset:str, inputs:list, miss_value:bool, data_scaling:str, training:int, validation:int, testing:int):
        # print(dataset, inputs, miss_value, data_scaling, training, validation, testing)

        global dataset_config

        data_summary_dict = get_data_setting(dataset, inputs, miss_value, data_scaling, training, validation, testing)

        # print(dataset, inputs, model_mapping[miss_value], model_mapping[data_scaling], [training/100, validation/100, testing/100])
        dataset_config=DatasetConfig(dataset, inputs, model_mapping[miss_value], model_mapping[data_scaling], [training/100, validation/100, testing/100])
        
        gr.Info("Setting Updated")
        return training_component.data_summary.update(value=data_summary_dict)

    def train_btn_click(select_model, dtc_criterion_dd, dtc_max_depth_tb, dtc_min_samples_split_sldr, dtc_min_samples_leaf_sldr, dtc_max_features_dd, dtc_max_leaf_nodes_tb, knc_althm_dd, knc_n_nbr_sldr, knc_weights_dd):
        
        global dataset_config
        output_list = []

        if select_model == "Decision Tree Classifier":
            dtc_max_features_dd = dtc_max_features_dd if dtc_max_features_dd != "None" else None
            model_config = DecisionTreeModelConfig(dtc_criterion_dd, dtc_min_samples_split_sldr, dtc_min_samples_leaf_sldr, dtc_max_features_dd, eval(dtc_max_depth_tb), eval(dtc_max_leaf_nodes_tb))
        elif select_model == "K Neighbor Classifier":
            model_config = KNNModelConfig(knc_n_nbr_sldr, knc_weights_dd, knc_althm_dd)
        
        figures, evaluations = training(dataset_config, model_config)

        evaluations = list(map(str,evaluations))

        img_components = [
            training_component.train_img1, 
            training_component.train_img2, 
            training_component.train_img3
        ]

        output_list.append(
            training_component.train_df.update(
                value=[evaluations]
            )
        )

        for i, component in enumerate(img_components):
            if figures[i] != None:
                output_list.append(component.update(value=figures[i], visible=True))
            else:
                output_list.append(component.update(visible=False))

        return *output_list,

    with gr.Blocks() as demo:
        get_header()
        with gr.Tab("Preprocess"):
            preprocessing_component = PreprocessingComponent()
            preprocessing_component.get_preprocessing()
            
        with gr.Tab("Training"):
            training_component = TrainingComponent()
            training_component.get_training()
                
        with gr.Tab("Result"):
            gr.Markdown(f"{page_content.explanatory_text['result']['title']}\n{page_content.explanatory_text['result']['body']}")
            with gr.Row():
                gr.Textbox("hi")
                gr.Textbox("hi")
            with gr.Row():
                gr.Textbox("hello")
                gr.Textbox("hello")
        
        model_components = {
            "all": [
                training_component.dtc_criterion_dd, 
                training_component.dtc_max_depth_tb, 
                training_component.dtc_min_samples_split_sldr, 
                training_component.dtc_min_samples_leaf_sldr, 
                training_component.dtc_max_features_dd, 
                training_component.dtc_max_leaf_nodes_tb, 
                training_component.knc_althm_dd, 
                training_component.knc_n_nbr_sldr, 
                training_component.knc_weights_dd
            ],
            "model_selector": [
                training_component.model_dd
            ],
            "decision_tree_classifier":[
                training_component.dtc_criterion_dd, 
                training_component.dtc_max_depth_tb, 
                training_component.dtc_min_samples_split_sldr, 
                training_component.dtc_min_samples_leaf_sldr, 
                training_component.dtc_max_features_dd, 
                training_component.dtc_max_leaf_nodes_tb
            ],
            "k_neighbors_classifier": [
                training_component.knc_althm_dd, 
                training_component.knc_n_nbr_sldr, 
                training_component.knc_weights_dd
            ],
        }

        preprocessing_component.submit_set_btn.click(
            fn=submit_setting_btn_click, 
            inputs=[
                preprocessing_component.dataset_dd, 
                preprocessing_component.inputs_dd, 
                preprocessing_component.miss_value_chkbox, 
                preprocessing_component.data_scale_dd, 
                preprocessing_component.train_sldr, 
                preprocessing_component.valid_sldr, 
                preprocessing_component.test_sldr
            ], 
            outputs=[training_component.data_summary]
        )
        training_component.train_btn.click(
            fn=train_btn_click, 
            inputs=[
                training_component.model_dd, 
                *model_components["all"]], 
            outputs=[
                training_component.train_df, 
                training_component.train_img1, 
                training_component.train_img2, 
                training_component.train_img3
            ]
        )
        
        training_component.model_dd.change(
            fn=model_dd_change, 
            inputs=training_component.model_dd, 
            outputs=model_components["all"]
        )

    demo.launch(
        # enable_queue=True, 
        debug=True,
        # share=True,
    )
