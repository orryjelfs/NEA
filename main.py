from physics_engine import PhysicsEngine

physics_engine = PhysicsEngine()

grid = physics_engine.generate_blanket_grid(depth_m=1.2, height_m=2.5)
print(grid)

physics_engine.calculate_attenuation(grid)
front_cell_flux = grid[0][0].neutron_flux
back_cell_flux = grid[0][-1].neutron_flux
print(f"Neutron flux at the front of the blanket: {front_cell_flux:.2e} neutrons/m^2/s")
print(f"Neutron flux at the back of the blanket: {back_cell_flux:.2e} neutrons/m^2/s")

physics_engine.calculate_tritium_production(grid)
print(f"Tritium production rate at the front of the blanket: {grid[0][0].tritium_production_rate:.2e} atoms/m^3/s")
print(f"Tritium production rate at the back of the blanket: {grid[0][-1].tritium_production_rate:.2e} atoms/m^3/s")