"""Heater control for the GHU-2 greenhouse (percent power, 0 to 100).

Owner: <name>
"""

from .helpers import _clamp

k_p = 0.1
k_i = 0.01
k_w = 0.0 # Integral Windup Term

total_error = 0.0

def control_heater(readings, setpoints, dt, state) -> float:
    """Return the heater power for this tick, a number in [0, 100].

    Parameters
    ----------
    readings : SensorReadings
        temperature_c, rh_pct, co2_ppm_primary (K30), co2_ppm_backup (SCD41),
        soil_vwc, par_umol_m2_s.
    setpoints : Setpoints
        temperature_c (day and night aware), co2_ppm, rh_pct, soil_vwc,
        is_daytime.
    dt : float
        The length of this tick in seconds (60 by default).
    state : dict
        A plain dictionary you may use to remember values between ticks. To
        keep a running total, read and write it like this:
        state["heater_total"] = state.get("heater_total", 0.0) + value.
        All four actuator files share this one dictionary, so start every key
        you use with this file's name, as "heater_total" does. Two files that
        both write state["total"] overwrite each other.

    Returns
    -------
    float
        Heater power percent, from 0 to 100.
    """
    # TODO: Replace this stub with your Milestone 3 heater design.
    # Your M3 flowchart is the specification. Keep each command in range
    # before you return it:
    #   1. At the top of this file, add "from .helpers import _clamp".
    #   2. Return "_clamp(u, 0.0, 100.0)", where u is your command.
    # That import only works when this file is loaded as part of the
    # student_controller package. Test it by running practice_test_m3.py or
    # practice_test_m4.py (or a script beside the package that imports it).
    # Pressing Run on this
    # file by itself stops with "attempted relative import with no known
    # parent package".
    
    error = setpoints.temperature_c - readings.temperature_c
    total_error = state.get("total_error", 0.0)
    
    raw = error * k_p + total_error * k_i    
    output = _clamp(error * k_p + total_error * k_i, 0.0, 100.0)
    
    saturation_error = output - raw
    
    state["total_error"] = total_error + error * dt + saturation_error * (k_w/k_i) * dt

    if(readings.temperature_c > setpoints.temperature_c * 0.99):
        output = 0.0

    return output
