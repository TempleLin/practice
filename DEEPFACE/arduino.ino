#include <FastLED.h>
#define NUM_LEDS 8
#define LED 7
String str;
CRGB leds[NUM_LEDS];
void setup() {
  FastLED.addLeds<NEOPIXEL, LED>(leds, NUM_LEDS);
  Serial.begin(9600);
}
void loop() {
  leds[0] = CRGB::Black;
  leds[1] = CRGB::Black;
  leds[2] = CRGB::Black;
  leds[3] = CRGB::Black;
  leds[4] = CRGB::Black;
  leds[5] = CRGB::Black;
  leds[6] = CRGB::Black;
  leds[7] = CRGB::Black;
  

  if (Serial.available()) {
    // 讀取傳入的字串直到"\n"結尾
    str = Serial.readStringUntil('\n');
    Serial.println(str);
    if (str == "0") {
        leds[0] = CRGB::White;
    } else if (str == "1") {
        leds[1] = CRGB::White;
    }else if (str == "2") {
        leds[2] = CRGB::White;
    }else if (str == "3") {
        leds[3] = CRGB::White;
    }
    else if (str == "4") {
        leds[4] = CRGB::White;
    }
    else if (str == "5") {
        leds[5] = CRGB::White;
    }
    else if (str == "6") {
        leds[6] = CRGB::White;
    }
    else if (str == "7") {
        leds[7] = CRGB::White;
    }
  }
  

  FastLED.show();
}