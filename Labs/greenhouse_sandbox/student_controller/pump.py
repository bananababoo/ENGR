"""Pump control for the GHU-2 greenhouse (percent speed, 0 to 100).

Owner: Dallas
"""



def control_pump(readings, setpoints, dt: float, state: dict) -> float:
    """Return the pump speed for this tick, a number in [0, 100].

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
        A plain dictionary you may use to remember values between ticks.
        All four actuator files share this one dictionary, so start every
        key you use with this file's name (for example, state["pump_total"]).
        Two files that both write state["total"] overwrite each other.

    Returns
    -------
    float
        Pump speed percent, from 0 to 100.
    """
    
    if(readings.soil_vwc < setpoints.soil_vwc * 0.7):
        state["pump_status"] = 15.0
    elif(readings.soil_vwc > setpoints.soil_vwc * 1.0):
        state["pump_status"] = 0.0
    
    return state.get("pump_status", 0.0)
