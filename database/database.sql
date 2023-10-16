USE emotion_recognizer;

CREATE TABLE audios (
  Audio_id varchar(50) NOT NULL,
  Audio_content mediumblob NOT NULL,
  Audio_name varchar(100) NOT NULL,
  PRIMARY KEY (Audio_id)
);

CREATE TABLE recognition (
  Audio_id varchar(50) NOT NULL,
  Emotion varchar(15) NOT NULL,
  Transcript text NOT NULL,
  Prediction varchar(5) NOT NULL,
  PRIMARY KEY (Audio_id)
);