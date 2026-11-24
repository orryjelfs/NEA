class Material:
    def __init__(self, li6_enrichment: float, be_fraction: float):
        self.li6_enrichment: float = li6_enrichment
        self.be_fraction: float = be_fraction

    #class constants
    atom_density: float = 4.6e28  #atoms/m^3
    microscopic_cross_section_li6: float = 940e-28  #m^2
    microscopic_cross_section_li7: float = 0.045e-28  #m^2
    microscopic_cross_section_be: float = 0.5e-28  #m^2

    def calculate_sigma_t(self):
        '''calculate the density of each material in the blanket'''
        be_density = self.atom_density * self.be_fraction
        remaining_density = self.atom_density * (1 - self.be_fraction)
        li6_density = remaining_density * self.li6_enrichment
        li7_density = remaining_density * (1 - self.li6_enrichment)

        '''calculate the macroscopic cross-section for each material'''
        sigma_t_be = be_density * self.microscopic_cross_section_be
        sigma_t_li6 = li6_density * self.microscopic_cross_section_li6
        sigma_t_li7 = li7_density * self.microscopic_cross_section_li7

        '''calculate the total macroscopic cross-section for tritium'''
        sigma_tritium = sigma_t_li6 + sigma_t_li7

        '''calculate the total macroscopic cross-section for the blanket'''
        sigma_t = sigma_t_be + sigma_tritium

        return sigma_t, sigma_tritium