from d3metafeatureextraction import D3MetafeatureExtraction

from d3m_metadata.container.pandas import DataFrame
from arff2pandas import a2p


if __name__ == '__main__':
    infile_path = "data/iris.arff"
    with open(infile_path, "r") as f:
        df = DataFrame(a2p.load(f)).rename(columns={"class@{Iris-setosa,Iris-versicolor,Iris-virginica}": "target"})

    metafeatures = D3MetafeatureExtraction(hyperparams=None).produce(inputs=df).value
    print(metafeatures)
