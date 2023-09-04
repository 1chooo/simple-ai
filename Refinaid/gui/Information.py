# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/31
Author: @1chooo(Hugo ChunHo Lin), @ReeveWu
Version: v0.0.7
'''

from typing import Any, Tuple

class PageContent:

    def __init__(self, *args: Any, **kwargs: Any) -> None:

        self.home_header = """\
        # Simple AI - Bridging the Gap with AI For Everyone

        Enabling everyone unfamiliar with programming languages \
        to easily engage with AI and open the doors to the world \
        of the future.
        """

        self.preprocessing_header = """\
        ## Data Preprocessing

        Let's begin exploring the data preprocessing of machine learning!
        """

        self.training_header = """\
        ## Training
        """

        self.dataset_choices = [
            "Titanic", 
            "Diabetes", 
            "House Prices",
        ]
