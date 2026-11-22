from blanket_cell import BlanketCell
from grid import Grid
from material import Material


class PhysicsEngine:
    def __init__(
        self, incident_flux: float = 1.0e18, depth_m: float = 1.2, height_m: float = 1.2
    ) -> None:
        # store the incident neutron flux for the blanket simulation
        self.incident_flux: float = incident_flux
        self._generate_blanket_grid(depth_m, height_m)

    def _generate_blanket_grid(
        self, depth_m: float = 1.2, height_m: float = 2.5
    ) -> None:
        DEPTH_COLS = 50
        HEIGHT_ROWS = 50

        dx = depth_m / DEPTH_COLS
        dy = height_m / HEIGHT_ROWS

        self._grid: list[list[BlanketCell]] = []
        for row in range(HEIGHT_ROWS):
            grid_row: list[BlanketCell] = []
            y_pos = (
                row + 0.5
            ) * dy  # calculate the center position of the cell in the y-direction
            for col in range(DEPTH_COLS):
                x_pos = (
                    col + 0.5
                ) * dx  # calculate the center position of the cell in the x-direction
                cell = BlanketCell(
                    depth_x=x_pos,
                    height_y=y_pos,
                    material=Material(li6_enrichment=0.0759, be_fraction=0.2),
                )
                grid_row.append(cell)
            self._grid.append(grid_row)

    def __repr__(self):
        return repr(self._grid)

    def calculate_attenuation(self) -> None:
        # calculate the attenuation of the neutron flux across the blanket grid
        for row in self._grid:
            # set the initial neutron flux for the first cell in each row
            current_flux = self.incident_flux
            for cell in row:
                # store incoming flux
                cell.neutron_flux = current_flux
                sigma_t = cell.sigma_t
                # calculate how much flux leaves the cell
                outgoing_flux = current_flux * math.exp((-1 * sigma_t) * cell.depth_x)
                # update the current flux for the next cell in the row
                current_flux = outgoing_flux
