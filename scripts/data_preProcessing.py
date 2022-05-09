import pandas as pd
import numpy as np


class data_preProcessing_script:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
################################################################################################
#  Data cleaning script
################################################################################################

    def drop_duplicates(self) -> pd.DataFrame:
        removables = self.df[self.df.duplicated()].index
        return self.df.drop(index=removables, inplace=True)

    def convert_to_numbers(self) -> pd.DataFrame:
        self.df = self.df.apply(pd.to_numeric, errors='coerce')
        return self.df


################################################################################################
#  Data Information script
################################################################################################

    def show_datatypes(self) -> pd.DataFrame:
        return self.df.dtypes

    def show_data_description(self) -> pd.DataFrame:
        return self.df.describe()

    def show_data_information(self) -> pd.DataFrame:
        return self.df.info()

    def show_statistical_info(self) -> pd.DataFrame:
        return self.df.agg(['mean'])

    def show_correlation(self) -> pd.DataFrame:
        return self.df.corr()

    def collective_grouped_mean(self, colomnName: str) -> pd.DataFrame:
        groupby_colomnName = self.df.groupby(colomnName)
        return groupby_colomnName.mean()

    def list_coloumn_names(self) -> pd.DataFrame:
        return self.df.columns


################################################################################################
#  Missing Data manipulation script
################################################################################################


################################################################################################
#  Visualization script
################################################################################################