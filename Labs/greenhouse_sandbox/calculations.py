surface_area = 43.2

battery_capacity_per_kg = 125 * .8 # wH/kg
hours_in_half_sol = 12.33  # One Martian night or day
hours_in_full_sol = 24.66  # One complete Martian sol
average_temperature_difference = 18 - (-37.5)
cold_night_temperature_difference = 18 - (-70)

led_fraction_heat = 0.35

standard_heater_watts = 2000
upgraded_heater_watts = 3000
led_watts = 600

standard_heater_mass = 6
upgraded_heater_mass = 9

def heat_loss_rate(thermal_transmittance, delta_t=cold_night_temperature_difference):
    return thermal_transmittance * surface_area * delta_t

def glazing_mass(mass_per_area):
    return mass_per_area * surface_area

def launch_cost(mass_val, cost_per_kg):
    return mass_val * cost_per_kg

def battery_mass(energy_usage):
    return energy_usage / battery_capacity_per_kg

heat_loss_rate_slpoly = heat_loss_rate(1.8)
heat_loss_rate_twpoly = heat_loss_rate(0.6)
heat_loss_rate_aerogel = heat_loss_rate(0.3)
heat_loss_rate_vip = heat_loss_rate(0.15)


print("Heat loss rate:")
print(f"- Single Layer polycarbonate: {heat_loss_rate_slpoly:.2f} W")
print(f"- Twin-wall polycarbonate: {heat_loss_rate_twpoly:.2f} W")
print(f"- Aerogel multi-layer: {heat_loss_rate_aerogel:.2f} W")
print(f"- Vacuum-insulated panel: {heat_loss_rate_vip:.2f} W")

usage_percentage_slpoly = 100 * heat_loss_rate_slpoly / standard_heater_watts
usage_percentage_twpoly = 100 * heat_loss_rate_twpoly / standard_heater_watts
usage_percentage_aerogel = 100 * heat_loss_rate_aerogel / standard_heater_watts
usage_percentage_vip = 100 * heat_loss_rate_vip / standard_heater_watts

usage_percentage_slpoly_upgraded = 100 * heat_loss_rate_slpoly / upgraded_heater_watts
usage_percentage_twpoly_upgraded = 100 * heat_loss_rate_twpoly / upgraded_heater_watts
usage_percentage_aerogel_upgraded = 100 * heat_loss_rate_aerogel / upgraded_heater_watts
usage_percentage_vip_upgraded = 100 * heat_loss_rate_vip / upgraded_heater_watts

print("\nUsage Percentage: ")
print("- Standard")
print(f"  - Single Layer polycarbonate: {usage_percentage_slpoly:.2f} %")
print(f"  - Twin-wall polycarbonate: {usage_percentage_twpoly:.2f} %")
print(f"  - Aerogel multi-layer: {usage_percentage_aerogel:.2f} %")
print(f"  - Vacuum-insulated panel: {usage_percentage_vip:.2f} %")
print()
print("- Upgraded")
print(f"  - Single Layer polycarbonate: {usage_percentage_slpoly_upgraded:.2f} %")
print(f"  - Twin-wall polycarbonate: {usage_percentage_twpoly_upgraded:.2f} %")
print(f"  - Aerogel multi-layer: {usage_percentage_aerogel_upgraded:.2f} %")
print(f"  - Vacuum-insulated panel: {usage_percentage_vip_upgraded:.2f} %")
print()

print("Nightly Heating Energy Usage:")
print(f"- Single Layer polycarbonate: {heat_loss_rate_slpoly * hours_in_half_sol:.2f} Wh")
print(f"- Twin-wall polycarbonate: {heat_loss_rate_twpoly * hours_in_half_sol:.2f} Wh")
print(f"- Aerogel multi-layer: {heat_loss_rate_aerogel * hours_in_half_sol:.2f} Wh")
print(f"- Vacuum-insulated panel: {heat_loss_rate_vip * hours_in_half_sol:.2f} Wh")

mass_per_area_slpoly = glazing_mass(2)
mass_per_area_twpoly = glazing_mass(3.5)
mass_per_area_aerogel = glazing_mass(8)
mass_per_area_vip = glazing_mass(12)

print("Mass for the whole surface:")
print(f"- Single Layer polycarbonate: {mass_per_area_slpoly:.2f} kg")
print(f"- Twin-wall polycarbonate: {mass_per_area_twpoly:.2f} kg")
print(f"- Aerogel multi-layer: {mass_per_area_aerogel:.2f} kg")
print(f"- Vacuum-insulated panel: {mass_per_area_vip:.2f} kg")
print()
print("Launch Cost for Glazing Mass:")
print(f"- Single Layer polycarbonate: {launch_cost(mass_per_area_slpoly, 50000):.2f}$")
print(f"- Twin-wall polycarbonate: {launch_cost(mass_per_area_twpoly, 50000):.2f}$")
print(f"- Aerogel multi-layer: {launch_cost(mass_per_area_aerogel, 50000):.2f}$")
print(f"- Vacuum-insulated panel: {launch_cost(mass_per_area_vip, 50000):.2f}$")

print()
print("Two best combos: Upgraded Twin Wall and Standard Aerogel")


avg_loss_twpoly = heat_loss_rate(0.6, average_temperature_difference)
avg_loss_aerogel = heat_loss_rate(0.3, average_temperature_difference)
    
upgraded_twin_wall_energy_usage = avg_loss_twpoly * hours_in_full_sol + led_watts * hours_in_full_sol / 2 - led_watts * hours_in_full_sol / 2 * led_fraction_heat
standard_aerogel_energy_usage = avg_loss_aerogel * hours_in_full_sol + led_watts * hours_in_full_sol / 2 - led_watts * hours_in_full_sol / 2 * led_fraction_heat

upgraded_aerogel_energy_usage = avg_loss_aerogel * hours_in_full_sol + led_watts * hours_in_full_sol / 2 - led_watts * hours_in_full_sol / 2 * led_fraction_heat
standard_twin_wall_energy_usage = avg_loss_twpoly * hours_in_full_sol + led_watts * hours_in_full_sol / 2 - led_watts * hours_in_full_sol / 2 * led_fraction_heat

print("Energy Usage for the Two Best Combos in a dust storm:")
print(f"- Upgraded Twin Wall {upgraded_twin_wall_energy_usage:.2f} Wh")
print(f"- Standard Aerogel {standard_aerogel_energy_usage:.2f} Wh")

print()

upgraded_twin_wall_battery_mass = battery_mass(upgraded_twin_wall_energy_usage)
standard_aerogel_battery_mass = battery_mass(standard_aerogel_energy_usage)

print("Battery Mass:")
print(f"- Upgraded Twin Wall: {upgraded_twin_wall_battery_mass :.2f} kg")
print(f"- Standard Aerogel: {standard_aerogel_battery_mass:.2f} kg")

upgraded_twin_wall_total_mass = mass_per_area_twpoly + upgraded_twin_wall_battery_mass + upgraded_heater_mass
standard_aerogel_total_mass = mass_per_area_aerogel + standard_aerogel_battery_mass + standard_heater_mass

print("Total Launch Mass:")
print(f"- Upgraded Twin Wall: {upgraded_twin_wall_total_mass:.2f} kg")
print(f"- Standard Aerogel: {standard_aerogel_total_mass:.2f} kg")

print("Total Launch Cost:")
print(f"- Upgraded Twin Wall: {launch_cost(upgraded_twin_wall_total_mass, 50000):.2f}$")
print(f"- Standard Aerogel: {launch_cost(standard_aerogel_total_mass, 50000):.2f}$")
