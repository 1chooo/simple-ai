class PageContent:

    def __init__(self) -> None:
        self.explanatory_text = {
            "header":{
                "title":"# Simple AI", 
                "body":"Enabling everyone unfamiliar with programming languages to easily engage with AI and open the doors to the world of the future."
            }, 
            "preprocess":{
                "title":"## What is preprocessing?", 
                "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."
            },
            "training":{
                "title":"## What is model training?", 
                "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."
            },
            "result":{
                "title":"## What is the result?", 
                "body":"Lorem ipsum dolor sit amet consectetur. Adipiscing commodo odio neque ut est scelerisque amet. Neque feugiat platea amet arcu et. Mi eget nisl magna diam et at elit ut vulputate. Vitae est integer a adipiscing sagittis integer ut facilisi interdum."
            },
        }

        self.dropdown_options = {
            "datasets": [
                "Titanic", 
                "Diabetes", 
                "House Prices",
            ],
            "inputs": [
                "ip1", 
                "ip2", 
                "ip3"
            ],
            "miss_value": ["Drop Nan", "By Columns"],
            "data_scalings": ["None", "Standard", "Min-Max"],
            "models": ["Decision Tree Classifier", "K Neighbor Classifier"],
            "plots": ["plot1", "plot2", "plot3"],
            "model_parameters":{
                                "decision_tree_classifier": {
                                    "criterion": ["gini", "entropy", "log_loss"],
                                    "max_features": ["None", "sqrt", "log2"]},
                                "k_neighbors_classifier": {
                                    "weights": ["uniform", "distance"],
                                    "algorithm": ["auto", "ball_tree", "kd_tree", "brute"]}
                                
            }

        }

        # self.model_parameters = {
        #                     "decision_tree_classifier": {
        #                                             "criterion": None,
        #                                             "max_depth": None,
        #                                             "min_samples_split": None,
        #                                             "min_samples_leaf": None,
        #                                             "max_features": None,
        #                                             "max_leaf_nodes": None
        #                     }
        # }