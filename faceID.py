int relayPin = 7;  // Relay connected to pin 7

void setup() {
  // Start serial communication
  Serial.begin(9600);
  
  // Set relay pin as output
  pinMode(relayPin, OUTPUT);
}

void loop() {
  // Check for incoming data (from Raspberry Pi or server)
  if (Serial.available() > 0) {
    String faceRecognitionResult = Serial.readString();  // Get the face recognition result
    
    // Check if the recognized face is authorized
    if (faceRecognitionResult == "AUTHORIZED") {
      // Unlock door (activate relay)
      digitalWrite(relayPin, HIGH);
      delay(5000);  // Keep the lock open for 5 seconds
      digitalWrite(relayPin, LOW);  // Lock door again
    }
    else {
      // Face not recognized, keep door locked
      digitalWrite(relayPin, LOW);
    }
  }
}
