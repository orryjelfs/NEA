from coord import Coord
from physics_engine import PhysicsEngine

physics_engine = PhysicsEngine(depth_m=1.2, height_m=2.5)

print(physics_engine)

front_cell = Coord(x=0, y=0)
back_cell = Coord(x=-1, y=0)

physics_engine.calculate_attenuation()
front_cell_flux = physics_engine.neutron_flux(front_cell)
back_cell_flux = physics_engine.neutron_flux(back_cell)

# front_cell_flux = .neutron_flux
# back_cell_flux = grid[0][-1].neutron_flux
print(f"Neutron flux at the front of the blanket: {front_cell_flux:.2e} neutrons/m^2/s")
print(f"Neutron flux at the back of the blanket: {back_cell_flux:.2e} neutrons/m^2/s")

physics_engine.calculate_tritium_production()
print(
    f"Tritium production rate at the front of the blanket: {physics_engine.tritium_production_rate(front_cell):.2e} atoms/m^3/s"
)
print(
    f"Tritium production rate at the back of the blanket: {physics_engine.tritium_production_rate(back_cell):.2e} atoms/m^3/s"
)
