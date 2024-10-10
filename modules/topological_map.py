from __future__ import annotations

import os
import pickle
from dataclasses import dataclass
from typing import List, Tuple

import networkx as nx
import torch


@dataclass(frozen=True)
class TopologicalMap:
    """Stores the topological map.

    Attributes:
        graph: NetworkX graph object
        nodes: List of the nodes of the graph
        gt_poses: List of the ground truth poses of the nodes
    """
    graph: nx.Graph
    nodes: List[torch.Tensor]
    gt_poses: List[Tuple[float, float, float]]

    def save(self, path: str) -> None:
        """Saves the topological map.

        Args:
            path: Path to save the topological map
        """

        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path: str) -> TopologicalMap:
        """Loads the topological map from a file.

        Args:
            path: Path to the file to be loaded

        Returns:
            TopologicalMap object

        Raises:
            FileNotFoundError: If the file does not exist
        """

        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist.")
        with open(path, "rb") as f:
            return pickle.load(f)