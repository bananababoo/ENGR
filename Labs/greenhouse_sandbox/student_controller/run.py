from martian_greenhouse_sim.simulation import (
    load_student_controller,
    load_student_hardware,
    run_simulation,
)

controller = load_student_controller(search_dirs=["."])
hardware = load_student_hardware(search_dirs=["."])
result = run_simulation(days=30, seed=42, controller_cls=controller, hardware=hardware)
print(result.summary())