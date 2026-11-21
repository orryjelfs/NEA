from blanket_cell import BlanketCell
from material import Material
import math
class PhysicsEngine:

    def __init__(self, incident_flux = 1.0e18):
        #store the incident neutron flux for the blanket simulation
        self.incident_flux = incident_flux

    def generate_blanket_grid(self, depth_m = 1.2, height_m = 2.5):
        DEPTH_COLS = 50
        HEIGHT_ROWS = 50

        dx = depth_m / DEPTH_COLS
        dy = height_m / HEIGHT_ROWS

        grid = []
        for row in range(HEIGHT_ROWS):
            grid_row = []
            y_pos = (row + 0.5) * dy #calculate the center position of the cell in the y-direction
            for col in range(DEPTH_COLS):
                x_pos = (col + 0.5) * dx #calculate the center position of the cell in the x-direction
                cell = BlanketCell(depth_x=x_pos, height_y=y_pos, material= Material(li6_enrichment=0.0759, be_fraction=0.2))
                grid_row.append(cell)
            grid.append(grid_row)

        return grid

    def calculate_attenuation(self, grid):
        #calculate the attenuation of the neutron flux across the blanket grid
        for row in grid:
            #set the initial neutron flux for the first cell in each row
            current_flux = self.incident_flux
            for cell in row:
                #store incoming flux
                cell.neutron_flux = current_flux
                sigma_t = cell.sigma_t
                #calculate how much flux leaves the cell
                outgoing_flux = current_flux * math.exp(-sigma_t * cell.depth_x)
                #update the current flux for the next cell in the row
                current_flux = outgoing_flux


physics_engine = PhysicsEngine()

grid = physics_engine.generate_blanket_grid(depth_m=1.2, height_m=2.5)
print(grid)

physics_engine.calculate_attenuation(grid)
front_cell_flux = grid[0][0].neutron_flux
back_cell_flux = grid[0][-1].neutron_flux
print(f"Neutron flux at the front of the blanket: {front_cell_flux:.2e} neutrons/m^2/s")
print(f"Neutron flux at the back of the blanket: {back_cell_flux:.2e} neutrons/m^2/s")
