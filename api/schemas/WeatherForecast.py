from marshmallow import Schema, fields, validate


# Schema for the 'location' object
class LocationSchema(Schema):
    name = fields.Str(required=True)
    region = fields.Str()
    country = fields.Str(required=True)
    lat = fields.Float()
    lon = fields.Float()
    tz_id = fields.Str()
    localtime_epoch = fields.Int()
    localtime = fields.Str()


# Schema for the 'condition' object
class ConditionSchema(Schema):
    text = fields.Str()
    icon = fields.Str()
    code = fields.Int()


# Schema for the 'air_quality' object
class AirQualitySchema(Schema):
    co = fields.Float()
    no2 = fields.Float()
    o3 = fields.Float()
    so2 = fields.Int()
    pm2_5 = fields.Float()
    pm10 = fields.Int()
    us_epa_index = fields.Int()
    gb_defra_index = fields.Int()


# Updated schema for the 'current' object
class CurrentSchema(Schema):
    last_updated_epoch = fields.Int()
    last_updated = fields.Str()
    temp_c = fields.Float()
    temp_f = fields.Float()
    is_day = fields.Int(validate=[validate.OneOf([0, 1])])
    condition = fields.Nested(ConditionSchema)
    wind_mph = fields.Float()
    wind_kph = fields.Float()
    wind_degree = fields.Int()
    wind_dir = fields.Str()
    pressure_mb = fields.Int()
    pressure_in = fields.Float()
    precip_mm = fields.Int()
    precip_in = fields.Int()
    humidity = fields.Int()
    cloud = fields.Int()
    feelslike_c = fields.Float()
    feelslike_f = fields.Float()
    vis_km = fields.Int()
    vis_miles = fields.Int()
    uv = fields.Float()
    gust_mph = fields.Float()
    gust_kph = fields.Float()


# Schema for each 'hour' inside 'forecast' -> 'forecastday'
class ForecastHourSchema(Schema):
    time_epoch = fields.Int()
    time = fields.Str()
    temp_c = fields.Float()
    temp_f = fields.Float()
    is_day = fields.Int(validate=[validate.OneOf([0, 1])])
    condition = fields.Nested(ConditionSchema)
    wind_mph = fields.Float()
    wind_kph = fields.Float()
    wind_degree = fields.Int()
    wind_dir = fields.Str()
    pressure_mb = fields.Float()
    pressure_in = fields.Float()
    precip_mm = fields.Float()
    precip_in = fields.Float()
    humidity = fields.Int()
    cloud = fields.Int()
    feelslike_c = fields.Float()
    feelslike_f = fields.Float()
    windchill_c = fields.Float()
    windchill_f = fields.Float()
    heatindex_c = fields.Float()
    heatindex_f = fields.Float()
    dewpoint_c = fields.Float()
    dewpoint_f = fields.Float()
    will_it_rain = fields.Int()
    chance_of_rain = fields.Int()
    will_it_snow = fields.Int()
    chance_of_snow = fields.Int()
    vis_km = fields.Int()
    vis_miles = fields.Int()
    gust_mph = fields.Float()
    gust_kph = fields.Float()
    uv = fields.Int()


# Schema for the 'day' object nested within 'forecast' -> 'forecastday'
class ForecastDayDetailsSchema(Schema):
    maxtemp_c = fields.Float()
    maxtemp_f = fields.Float()
    mintemp_c = fields.Float()
    mintemp_f = fields.Float()
    avgtemp_c = fields.Float()
    avgtemp_f = fields.Float()
    maxwind_mph = fields.Float()
    maxwind_kph = fields.Float()
    totalprecip_mm = fields.Float()
    totalprecip_in = fields.Float()
    totalsnow_cm = fields.Float()
    avgvis_km = fields.Float()
    avgvis_miles = fields.Float()
    avghumidity = fields.Float()
    daily_will_it_rain = fields.Int()
    daily_chance_of_rain = fields.Int()
    daily_will_it_snow = fields.Int()
    daily_chance_of_snow = fields.Int()
    condition = fields.Nested(ConditionSchema)
    uv = fields.Float()


# Schema for each 'forecastday' inside 'forecast'
class ForecastDaySchema(Schema):
    date = fields.Str()
    date_epoch = fields.Int()
    day = fields.Nested(ForecastDayDetailsSchema)
    astro = fields.Dict()
    hour = fields.List(fields.Nested(ForecastHourSchema))


# Schema for the 'forecast' object
class ForecastSchema(Schema):
    forecastday = fields.List(fields.Nested(ForecastDaySchema))


# Schema for each 'alert' inside 'alerts'
class AlertSchema(Schema):
    headline = fields.Str()
    msgtype = fields.Str(allow_none=True)
    severity = fields.Str(allow_none=True)
    urgency = fields.Str(allow_none=True)
    areas = fields.Str(allow_none=True)
    category = fields.Str()
    certainty = fields.Str(allow_none=True)
    event = fields.Str()
    note = fields.Str(allow_none=True)
    effective = fields.Str()
    expires = fields.Str()
    desc = fields.Str()
    instruction = fields.Str(allow_none=True)


# Schema for the 'alerts' object
class AlertsSchema(Schema):
    alert = fields.List(fields.Nested(AlertSchema))


# Main schema comprising all the above schemas
class WeatherForecast(Schema):
    """
    Represents the schema for a Weather object. This is used to validate
    return data from the Weather API.
    """

    location = fields.Nested(LocationSchema, required=True)
    current = fields.Nested(CurrentSchema)
    forecast = fields.Nested(ForecastSchema)
    alerts = fields.Nested(AlertsSchema)
