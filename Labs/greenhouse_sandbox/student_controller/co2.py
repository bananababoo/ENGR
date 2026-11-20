"""CO2 valve control for the GHU-2 greenhouse (percent open, 0 to 100).

Owner: Evan
"""

from .helpers import _clamp

k_p = 0.1

def control_co2(readings, setpoints, dt: float, state: dict) -> float:
    """Return the CO2 valve opening for this tick, a number in [0, 100].

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
        key you use with this file's name (for example, state["co2_total"]).
        Two files that both write state["total"] overwrite each other.

    Returns
    -------
    float
        CO2 valve opening percent, from 0 to 100.
    """
    co2_reading = 0.0
    
    if(abs(readings.co2_ppm_primary - readings.co2_ppm_backup) > 200):
        co2_reading = readings.co2_ppm_backup
    else:
        co2_reading = (readings.co2_ppm_primary + readings.co2_ppm_backup) / 2.0
    
    error = setpoints.co2_ppm - co2_reading
    
    return _clamp(error * k_p, 0.0, 100.0)
