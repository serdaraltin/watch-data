CREATE TABLE "Company" (
  "company_id" SERIAL PRIMARY KEY,
  "name" VARCHAR(255) NOT NULL,
  "registration_number" VARCHAR(20) UNIQUE,
  "industry" VARCHAR(100),
  "website" VARCHAR(255),
  "phone_number" VARCHAR(20),
  "address" VARCHAR(255),
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE "Branch" (
  "branch_id" SERIAL PRIMARY KEY,
  "company_id" INT,
  "parent_branch_id" INT,
  "name" VARCHAR(255) NOT NULL,
  "location" VARCHAR(255),
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("company_id", "branch_id")
);

CREATE TABLE "Camera" (
  "camera_id" SERIAL PRIMARY KEY,
  "branch_id" INT,
  "model" VARCHAR(255) NOT NULL,
  "resolution" VARCHAR(20),
  "install_date" DATE,
  "status" VARCHAR(20),
  "streaming_url" VARCHAR(255),
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("branch_id", "camera_id")
);

CREATE TABLE "Incident" (
  "incident_id" SERIAL PRIMARY KEY,
  "camera_id" INT,
  "incident_date" TIMESTAMP,
  "description" TEXT,
  "resolved" BOOLEAN,
  "resolution_details" TEXT,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("camera_id", "incident_id")
);

CREATE TABLE "AppUser" (
  "user_id" SERIAL PRIMARY KEY,
  "branch_id" INT,
  "username" VARCHAR(50) UNIQUE,
  "password_hash" VARCHAR(255) NOT NULL,
  "email" VARCHAR(255),
  "full_name" VARCHAR(100),
  "role" VARCHAR(20),
  "last_login" TIMESTAMP,
  "account_status" VARCHAR(20),
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("user_id", "branch_id")
);

CREATE TABLE "UserCameraAccess" (
  "access_id" SERIAL PRIMARY KEY,
  "user_id" INT,
  "camera_id" INT,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("user_id", "camera_id")
);

CREATE TABLE "Person" (
  "person_id" SERIAL PRIMARY KEY,
  "camera_id" INT,
  "detection_time" TIMESTAMP,
  "label" TEXT,
  "confidence" DECIMAL(5,4),
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("camera_id", "person_id")
);

CREATE TABLE "EnterExit" (
  "enter_exit_id" SERIAL PRIMARY KEY,
  "person_id" INT,
  "event_time" TIMESTAMP,
  "event_type" VARCHAR(10),
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("person_id", "enter_exit_id")
);

CREATE TABLE "Gender" (
  "gender_id" SERIAL PRIMARY KEY,
  "person_id" INT,
  "gender" TEXT,
  "confidence" DECIMAL(5,4),
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("person_id", "gender_id")
);

CREATE TABLE "Age" (
  "age_id" SERIAL PRIMARY KEY,
  "person_id" INT,
  "age_range" VARCHAR(20),
  "confidence" DECIMAL(5,4),
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("person_id", "age_id")
);

CREATE TABLE "Movement" (
  "movement_id" SERIAL PRIMARY KEY,
  "person_id" INT,
  "movement_type" VARCHAR(20),
  "start_time" TIMESTAMP,
  "end_time" TIMESTAMP,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("person_id", "movement_id")
);

CREATE TABLE "SecurityLog" (
  "log_id" SERIAL PRIMARY KEY,
  "user_id" INT,
  "action_description" TEXT,
  "log_time" TIMESTAMP,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("user_id", "log_id")
);

CREATE TABLE "MaintenanceLog" (
  "log_id" SERIAL PRIMARY KEY,
  "camera_id" INT,
  "action_description" TEXT,
  "log_time" TIMESTAMP,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("camera_id", "log_id")
);

CREATE TABLE "Density" (
  "density_id" SERIAL PRIMARY KEY,
  "camera_id" INT,
  "status" BOOLEAN,
  "additional" JSON,
  "label" TEXT,
  "created_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updated_at" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("camera_id")
);

ALTER TABLE "Branch" ADD FOREIGN KEY ("company_id") REFERENCES "Company" ("company_id");

ALTER TABLE "Branch" ADD FOREIGN KEY ("parent_branch_id") REFERENCES "Branch" ("branch_id");

ALTER TABLE "Camera" ADD FOREIGN KEY ("branch_id") REFERENCES "Branch" ("branch_id");

ALTER TABLE "AppUser" ADD FOREIGN KEY ("branch_id") REFERENCES "Branch" ("branch_id");

ALTER TABLE "UserCameraAccess" ADD FOREIGN KEY ("user_id") REFERENCES "AppUser" ("user_id");

ALTER TABLE "UserCameraAccess" ADD FOREIGN KEY ("camera_id") REFERENCES "Camera" ("camera_id");

ALTER TABLE "Person" ADD FOREIGN KEY ("camera_id") REFERENCES "Camera" ("camera_id");

ALTER TABLE "EnterExit" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("person_id");

ALTER TABLE "Gender" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("person_id");

ALTER TABLE "Age" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("person_id");

ALTER TABLE "Movement" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("person_id");

ALTER TABLE "SecurityLog" ADD FOREIGN KEY ("user_id") REFERENCES "AppUser" ("user_id");

ALTER TABLE "MaintenanceLog" ADD FOREIGN KEY ("camera_id") REFERENCES "Camera" ("camera_id");

ALTER TABLE "Camera" ADD FOREIGN KEY ("camera_id") REFERENCES "Incident" ("camera_id");

ALTER TABLE "Density" ADD FOREIGN KEY ("camera_id") REFERENCES "Camera" ("camera_id");
