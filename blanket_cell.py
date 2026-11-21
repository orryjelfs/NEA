class BlanketCell:
    #represetnts a single cell in the blanket grid
    def __init__(self, depth_x, height_y, material):
        self.depth_x = depth_x
        self.height_y = height_y
        self.material = material

        self.neutron_flux = 0.0
        self.tritium_production_rate = 0.0

    @property
    #returns the total macroscopic cross-section for the blanket cell when accessed
    def sigma_t(self):
        sigma_t, _ = self.material.calculate_sigma_t()
        return sigma_t

    @property
    #returns the macroscopic cross-section for tritium production when accessed
    def sigma_tritium(self):
        _, sigma_tritium = self.material.calculate_sigma_t()
        return sigma_tritium

    def __repr__(self):
        #represents the BlanketCell object as a string
        return f"BlanketCell(x={self.depth_x:.3f}m, y={self.height_y:.3f}m)"