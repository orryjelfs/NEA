from material import Material


class BlanketCell:
    """represetnts a single cell in the blanket grid"""

    def __init__(self, depth_x: float, height_y: float, material: Material) -> None:
        self.depth_x: float = depth_x
        self.height_y: float = height_y
        self.material: Material = material

        self.neutron_flux: float = 0.0
        self.tritium_production_rate: float = 0.0

    @property
    def sigma_t(self) -> float:
        """returns the total macroscopic cross-section for the blanket cell when accessed"""
        sigma_t, _ = self.material.calculate_sigma_t()
        return sigma_t

    @property
    def sigma_tritium(self) -> float:
        """returns the macroscopic cross-section for tritium production when accessed"""
        _, sigma_tritium = self.material.calculate_sigma_t()
        return sigma_tritium

    def __repr__(self) -> str:
        """represents the BlanketCell object as a string"""
        return f"BlanketCell(x={self.depth_x:.3f}m, y={self.height_y:.3f}m)"
