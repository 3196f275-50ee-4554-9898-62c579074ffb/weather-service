# Weather Service

Сервис реализующий REST API GET запрос для получения массива координат и температуры в точке http://127.0.0.1:5000/weather, а также GET запрос для получения отрендеренной карты краснодара с Pointers хранимыми температура http://127.0.0.1:5000/map. 

Install depends:
```bash
pip install requests Flask folium
```

![map.png](__assets__%2Fmap.png)

```json
{
  "Adygeysk": {
    "lat": 44.88,
    "lon": 39.19,
    "temp": 23.9
  },
  "Afipskiy": {
    "lat": 44.9021,
    "lon": 38.8439,
    "temp": 23.36
  },
  "Agronom": {
    "lat": 45.1387,
    "lon": 39.1939,
    "temp": 23.94
  },
  "Andreyevskaya": {
    "lat": 45.31,
    "lon": 38.66,
    "temp": 23.45
  },
  "Azovskaya": {
    "lat": 44.7908,
    "lon": 38.6264,
    "temp": 23.08
  },
  "Beloz\u00ebrnyy": {
    "lat": 45.0643,
    "lon": 38.679,
    "temp": 23.42
  },
  "Boykoponura": {
    "lat": 45.3492,
    "lon": 38.7715,
    "temp": 23.42
  },
  "Dinskaya": {
    "lat": 45.2178,
    "lon": 39.2283,
    "temp": 23.97
  },
  "Enem": {
    "lat": 44.9271,
    "lon": 38.9085,
    "temp": 23.34
  },
  "Il'skiy": {
    "lat": 44.8422,
    "lon": 38.5669,
    "temp": 23.02
  },
  "Kalinino": {
    "lat": 59.6167,
    "lon": 42.25,
    "temp": 16.83
  },
  "Kaluzhskaya": {
    "lat": 44.7681,
    "lon": 38.9739,
    "temp": 23.74
  },
  "Karla Marksa": {
    "lat": 56.6,
    "lon": 36.6167,
    "temp": 18.95
  },
  "Kazazov": {
    "lat": 44.9033,
    "lon": 39.1742,
    "temp": 23.96
  },
  "Kochkin": {
    "lat": 44.8661,
    "lon": 39.1867,
    "temp": 23.9
  },
  "Krasnodar": {
    "lat": 45,
    "lon": 40,
    "temp": 19.54
  },
  "Lakshukay": {
    "lat": 44.95,
    "lon": 39.1331,
    "temp": 24.04
  },
  "Lazurnyy": {
    "lat": 45.1444,
    "lon": 39.0894,
    "temp": 23.99
  },
  "Lenina": {
    "lat": 46.0667,
    "lon": 39.7833,
    "temp": 21.03
  },
  "Leninskiy": {
    "lat": 54.2781,
    "lon": 37.4558,
    "temp": 18.8
  },
  "Mol\u2019kin": {
    "lat": 44.8022,
    "lon": 39.2372,
    "temp": 23.95
  },
  "Novaya Adygeya": {
    "lat": 45.02,
    "lon": 38.9378,
    "temp": 23.39
  },
  "Novodmitriyevskaya": {
    "lat": 44.8347,
    "lon": 38.8772,
    "temp": 23.27
  },
  "Novomyshastovskaya": {
    "lat": 45.1991,
    "lon": 38.5827,
    "temp": 23.43
  },
  "Novotitarovskaya": {
    "lat": 45.2356,
    "lon": 38.9792,
    "temp": 23.36
  },
  "Novovelichkovskaya": {
    "lat": 45.2778,
    "lon": 38.8436,
    "temp": 23.39
  },
  "Novyy": {
    "lat": 45.0072,
    "lon": 38.9819,
    "temp": 23.39
  },
  "Oktyabr\u2019skiy": {
    "lat": 54.4815,
    "lon": 53.471,
    "temp": 18.16
  },
  "Pashkovskiy": {
    "lat": 45.0231,
    "lon": 39.1061,
    "temp": 24
  },
  "Plastunovskaya": {
    "lat": 45.2939,
    "lon": 39.2669,
    "temp": 23.94
  },
  "Pobeditel\u2019": {
    "lat": 45.1236,
    "lon": 39.1003,
    "temp": 23.97
  },
  "Ponezhukay": {
    "lat": 44.8876,
    "lon": 39.3855,
    "temp": 23.94
  },
  "Psekups": {
    "lat": 44.8314,
    "lon": 39.2114,
    "temp": 23.98
  },
  "Rossiyskiy": {
    "lat": 45.1144,
    "lon": 39.0386,
    "temp": 23.29
  },
  "Severskaya": {
    "lat": 44.8541,
    "lon": 38.6769,
    "temp": 23.18
  },
  "Smolenskaya": {
    "lat": 44.7887,
    "lon": 38.8018,
    "temp": 23.2
  },
  "Sorokin": {
    "lat": 52.1578,
    "lon": 34.0367,
    "temp": 16.81
  },
  "Starokorsunskaya": {
    "lat": 45.0573,
    "lon": 39.3161,
    "temp": 23.96
  },
  "Staromyshastovskaya": {
    "lat": 45.3433,
    "lon": 39.0761,
    "temp": 23.35
  },
  "Takhtamukay": {
    "lat": 44.9215,
    "lon": 38.9958,
    "temp": 23.28
  },
  "Tlyustenkhabl'": {
    "lat": 44.98,
    "lon": 39.0972,
    "temp": 24.08
  },
  "Tugurgoy": {
    "lat": 44.9508,
    "lon": 39.1161,
    "temp": 24.06
  },
  "Vasyurinskaya": {
    "lat": 45.1181,
    "lon": 39.424,
    "temp": 23.94
  },
  "Vitim": {
    "lat": 59.4511,
    "lon": 112.5578,
    "temp": 7.94
  },
  "Vorontsovskaya": {
    "lat": 45.2213,
    "lon": 38.7377,
    "temp": 23.39
  },
  "Yablonovsky": {
    "lat": 44.989,
    "lon": 38.9432,
    "temp": 23.39
  },
  "Yelizavetinskaya": {
    "lat": 45.0445,
    "lon": 38.7958,
    "temp": 23.38
  },
  "Yuzhnyy": {
    "lat": 53.2542,
    "lon": 83.6936,
    "temp": 23.21
  },
  "Znamenskiy": {
    "lat": 45.0556,
    "lon": 39.1497,
    "temp": 23.96
  },
  "Zonal\u2019nyy": {
    "lat": 45.0872,
    "lon": 39.1211,
    "temp": 23.97
  }
}
```