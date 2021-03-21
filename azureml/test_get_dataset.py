from azureml.core import Workspace, Datastore, Dataset

ws = Workspace.from_config()

dataset = Dataset.get_by_name(ws, name="test_data")
df = dataset.to_pandas_dataframe()
print(df.head())