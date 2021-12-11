CREATE TABLE STADIUM (
Stadium_id INT PRIMARY KEY,
Stadium_name VARCHAR(45),
Capacity VARCHAR(45)
);

CREATE TABLE CLUB_INFO(
Club_id INT PRIMARY KEY,
Club_name VARCHAR(45),
Stadium INT,
Club_url VARCHAR(45),
Club_badge_image VARCHAR(45),
FOREIGN KEY(Stadium) REFERENCES STADIUM(Stadium_id)
);

CREATE TABLE PLAYER(
Player_id INT PRIMARY KEY ,
Club_id INT,
Player_name VARCHAR(45),
Uniform_num INT check (Uniform_num >= 1, Uniform_num<=100),
Date_of_birth VARCHAR(45),
position VARCHAR(45),
FOREIGN KEY(Club_id) REFERENCES CLUB_INFO(Club_id)
);

CREATE TABLE CLUB_RESULT(
Club_id INT PRIMARY KEY,
position INT,
played INT,
Won INT,
Drawn INT,
lost INT,
ga INT,
gf INT,
Form VARCHAR(45),
FOREIGN KEY(Club_id) REFERENCES CLUB_INFO(Club_id)
);
