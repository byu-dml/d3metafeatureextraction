import pandas as pd

from d3m_metadata.container.pandas import DataFrame

from d3metafeatureextraction import D3MetafeatureExtraction

if __name__ == '__main__':
    infile_path = "data/38_sick_train_data.csv"
    df = DataFrame(pd.read_csv(infile_path))
    df = df.rename(columns={"Class": "target"})
    df.drop("d3mIndex", axis=1, inplace=True)
    metafeatures = D3MetafeatureExtraction(hyperparams=None).produce(inputs=df).value
    print(metafeatures)
