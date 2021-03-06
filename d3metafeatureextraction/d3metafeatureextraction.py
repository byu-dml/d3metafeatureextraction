import typing

import d3m_metadata
from primitive_interfaces.base import CallResult
from primitive_interfaces.featurization import FeaturizationTransformerPrimitiveBase

from metalearn.metafeatures.simple_metafeatures import SimpleMetafeatures
from metalearn.metafeatures.statistical_metafeatures import StatisticalMetafeatures
from metalearn.metafeatures.information_theoretic_metafeatures import InformationTheoreticMetafeatures
from metalearn.metafeatures.landmarking_metafeatures import LandmarkingMetafeatures

import pandas as pd

__version__ = "0.2.0"

Inputs = d3m_metadata.container.pandas.DataFrame
Outputs = d3m_metadata.container.pandas.DataFrame
class Hyperparams(d3m_metadata.hyperparams.Hyperparams):
    # could be used to determine which metafeatures to compute
    pass

class D3MetafeatureExtraction(FeaturizationTransformerPrimitiveBase[Inputs, Outputs, Hyperparams]):

    # This should contain only metadata which cannot be automatically determined from the code.
    metadata = d3m_metadata.metadata.PrimitiveMetadata({
        "primitive_code": {
            "interfaces_version": "2018.1.26"
        },
        "source": {
            "name": "byu-dml",
            "contact": "https://github.com/byu-dml"
        },
        "python_path": "d3m.primitives.d3metafeatureextraction.D3MetafeatureExtraction",
        "version": "v{}".format(__version__),
        "installation": [
            {
                "type": "PIP",
                "package": "d3metafeatureextraction",
                "version": str(__version__)
            }
        ],
        "primitive_family": "METAFEATURE_EXTRACTION",
        "algorithm_types": [
            "DATA_PROFILING",
            "CANONICAL_CORRELATION_ANALYSIS",
            "INFORMATION_ENTROPY",
            "MUTUAL_INFORMATION",
            "SIGNAL_TO_NOISE_RATIO",
            "STATISTICAL_MOMENT_ANALYSIS"
        ],
        "id": "28d12214-8cb0-4ac0-8946-d31fcbcd4142",
        "name": "Dataset Metafeature Extraction"
    })

    def __init__(self, *, hyperparams: Hyperparams, random_seed: int = 0, docker_containers: typing.Dict[str, str] = None) -> None:
        super().__init__(hyperparams=hyperparams, random_seed=random_seed, docker_containers=docker_containers)

    def produce(self, *, inputs: Inputs, timeout: float = None, iterations: int = None) -> CallResult[Outputs]:
        """
        Produce primitive's best choice of the output for each of the inputs.

        The output value should be wrapped inside ``CallResult`` object before returning.

        In many cases producing an output is a quick operation in comparison with ``fit``, but not
        all cases are like that. For example, a primitive can start a potentially long optimization
        process to compute outputs. ``timeout`` and ``iterations`` can serve as a way for a caller
        to guide the length of this process.

        Ideally, a primitive should adapt its call to try to produce the best outputs possible
        inside the time allocated. If this is not possible and the primitive reaches the timeout
        before producing outputs, it should raise a ``TimeoutError`` exception to signal that the
        call was unsuccessful in the given time. The state of the primitive after the exception
        should be as the method call has never happened and primitive should continue to operate
        normally. The purpose of ``timeout`` is to give opportunity to a primitive to cleanly
        manage its state instead of interrupting execution from outside. Maintaining stable internal
        state should have precedence over respecting the ``timeout`` (caller can terminate the
        misbehaving primitive from outside anyway). If a longer ``timeout`` would produce
        different outputs, then ``CallResult``'s ``has_finished`` should be set to ``False``.

        Some primitives have internal iterations (for example, optimization iterations).
        For those, caller can provide how many of primitive's internal iterations
        should a primitive do before returning outputs. Primitives should make iterations as
        small as reasonable. If ``iterations`` is ``None``, then there is no limit on
        how many iterations the primitive should do and primitive should choose the best amount
        of iterations on its own (potentially controlled through hyper-parameters).
        If ``iterations`` is a number, a primitive has to do those number of iterations,
        if possible. ``timeout`` should still be respected and potentially less iterations
        can be done because of that. Primitives with internal iterations should make
        ``CallResult`` contain correct values.

        For primitives which do not have internal iterations, any value of ``iterations``
        means that they should run fully, respecting only ``timeout``.

        Parameters
        ----------
        inputs : Inputs
            The inputs of shape [num_inputs, ...].
        timeout : float
            A maximum time this primitive should take to produce outputs during this method call, in seconds.
        iterations : int
            How many of internal iterations should the primitive do.

        Returns
        -------
        CallResult[Outputs]
            The outputs of shape [num_inputs, ...] wrapped inside ``CallResult``.
        """
        if not isinstance(inputs, d3m_metadata.container.pandas.DataFrame):
            raise ValueError("inputs must be an instance of 'd3m_metadata.container.pandas.DataFrame'")
        if "target" not in inputs.columns:
            raise ValueError("inputs must contain single-class classification targets in a column labeled 'target'")

        simple_metafeatures = SimpleMetafeatures().compute(inputs)
        statistical_metafeatures = StatisticalMetafeatures().compute(inputs)
        information_thoeretic_metafeatures = InformationTheoreticMetafeatures().compute(inputs)
        landmarking_metafeatures = LandmarkingMetafeatures().compute(inputs)

        metafeatures_df = d3m_metadata.container.pandas.DataFrame(pd.concat([
            simple_metafeatures,
            statistical_metafeatures,
            information_thoeretic_metafeatures,
            landmarking_metafeatures
        ], axis=1))

        return CallResult(metafeatures_df)
