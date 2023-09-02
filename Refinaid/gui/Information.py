# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.1
'''

class PageContent:

    def __init__(self) -> None:

        self.home_header = """\
        # Simple AI - Bridging the Gap with AI For Everyone

        Enabling everyone unfamiliar with programming languages \
        to easily engage with AI and open the doors to the world \
        of the future.
        """

        self.preprocessing_header = """\
        ## Preprocessing
        """

        self.explanatory_text = {
            "header": {
                "title": "# Simple AI - Bridging the Gap with AI For Everyone", 
                "body": """Enabling everyone unfamiliar with programming languages to easily engage with AI and open the doors to the world of the future."""
            }, 
            "preprocess": {
                "title": "## Try observing the data!", 
                "body": ""
            },
            "training": {
                "title": "## Model Training Demystified", 
                "body": ""
            },
            "result": {
                "title": "## What You Have Done?", 
                "body": ""
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
            "miss_value": [
                "Drop Nan", 
                "By Columns"
            ],
            "data_scalings": [
                "None", 
                "Standard", 
                "Min-Max"
            ],
            "models": [
                "Decision Tree Classifier", 
                "K Neighbor Classifier",
            ],
            "plots": [
                "plot1", 
                "plot2", 
                "plot3"
            ],
            "model_parameters":{
                "decision_tree_classifier": {
                    "criterion": [
                        "gini", 
                        "entropy", 
                        "log_loss"
                    ],
                    "max_features": [
                        "None", 
                        "sqrt", 
                        "log2"
                    ],
                },
                "k_neighbors_classifier": {
                    "weights": [
                        "uniform", 
                        "distance"
                    ],
                    "algorithm": [
                        "auto", 
                        "ball_tree", 
                        "kd_tree", 
                        "brute"
                    ],
                }
                                
            }

        }
