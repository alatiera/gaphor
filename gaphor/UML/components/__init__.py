from gaphor.UML.components.artifact import ArtifactItem
from gaphor.UML.components.component import ComponentItem
from gaphor.UML.components.connector import ConnectorItem
from gaphor.UML.components.node import NodeItem


def _load():
    from gaphor.UML.components import (
        componentsgrouping,
        connectorconnect,
        componentspropertypage,
    )


_load()