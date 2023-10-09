CREATE DATABASE IF NOT EXISTS emotion_recognizer;
USE emotion_recognizer;

CREATE TABLE IF NOT EXISTS audios (
  Cod_files varchar(50) NOT NULL,
  Audios_files mediumblob NOT NULL,
  Desc_Files varchar(100) NOT NULL,
  PRIMARY KEY (Cod_files)
);

CREATE TABLE IF NOT EXISTS recognition (
  File_id varchar(50) NOT NULL,
  Emotion varchar(15) NOT NULL,
  Transcript text NOT NULL,
  Percentage varchar(5) NOT NULL,
  PRIMARY KEY (File_id)
);