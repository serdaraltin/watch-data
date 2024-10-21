CREATE TABLE "Company" (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(255) NOT NULL,
  "registration_number" VARCHAR(20) UNIQUE,
  "industry" VARCHAR(100),
  "website" VARCHAR(255),
  "phone_number" VARCHAR(20),
  "address" VARCHAR(255),
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE "Branch" (
  "id" SERIAL PRIMARY KEY,
  "company_id" INT,
  "parent_branch_id" INT,
  "name" VARCHAR(255) NOT NULL,
  "location" VARCHAR(255),
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("company_id", "id")
);

CREATE TABLE "Camera" (
  "id" SERIAL PRIMARY KEY,
  "branch_id" INT,
  "model" VARCHAR(255) NOT NULL,
  "resolution" VARCHAR(20),
  "install_date" DATE,
  "status" VARCHAR(20),
  "protocol" VARCHAR(255) NOT NULL,
  "streaming_url" VARCHAR(255),
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("branch_id", "id")
);

CREATE TABLE "Incident" (
  "id" SERIAL PRIMARY KEY,
  "camera_id" INT,
  "incident_date" TIMESTAMP,
  "description" TEXT,
  "resolved" BOOLEAN,
  "resolution_details" TEXT,
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("camera_id", "id")
);

CREATE TABLE "AppUser" (
  "id" SERIAL PRIMARY KEY,
  "branch_id" INT,
  "username" VARCHAR(50) UNIQUE,
  "password_hash" VARCHAR(255) NOT NULL,
  "email" VARCHAR(255),
  "full_name" VARCHAR(100),
  "role" VARCHAR(20),
  "last_login" TIMESTAMP,
  "account_status" VARCHAR(20),
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("id", "branch_id")
);

CREATE TABLE "UserCameraAccess" (
  "id" SERIAL PRIMARY KEY,
  "user_id" INT,
  "camera_id" INT,
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("user_id", "id")
);

CREATE TABLE "Person" (
  "id" SERIAL PRIMARY KEY,
  "camera_id" INT,
  "detection_time" TIMESTAMP,
  "label" TEXT,
  "confidence" DECIMAL(5,4),
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("camera_id", "id")
);

CREATE TABLE "EnterExit" (
  "id" SERIAL PRIMARY KEY,
  "person_id" INT,
  "event_time" TIMESTAMP,
  "event_type" VARCHAR(10),
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("person_id", "id")
);

CREATE TABLE "Gender" (
  "id" SERIAL PRIMARY KEY,
  "person_id" INT,
  "gender" TEXT,
  "confidence" DECIMAL(5,4),
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("person_id", "id")
);

CREATE TABLE "Age" (
  "id" SERIAL PRIMARY KEY,
  "person_id" INT,
  "age_range" VARCHAR(20),
  "confidence" DECIMAL(5,4),
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("person_id", "id")
);

CREATE TABLE "Movement" (
  "id" SERIAL PRIMARY KEY,
  "person_id" INT,
  "movement_type" VARCHAR(20),
  "start_time" TIMESTAMP,
  "end_time" TIMESTAMP,
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("person_id", "id")
);

CREATE TABLE "SecurityLog" (
  "id" SERIAL PRIMARY KEY,
  "user_id" INT,
  "action_description" TEXT,
  "log_time" TIMESTAMP,
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("user_id", "id")
);

CREATE TABLE "MaintenanceLog" (
  "id" SERIAL PRIMARY KEY,
  "camera_id" INT,
  "action_description" TEXT,
  "log_time" TIMESTAMP,
  "createdAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  "updateAt" TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  PRIMARY KEY ("camera_id", "id")
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

ALTER TABLE "Branch" ADD FOREIGN KEY ("company_id") REFERENCES "Company" ("id");

ALTER TABLE "Branch" ADD FOREIGN KEY ("parent_branch_id") REFERENCES "Branch" ("id");

ALTER TABLE "Camera" ADD FOREIGN KEY ("branch_id") REFERENCES "Branch" ("id");

ALTER TABLE "AppUser" ADD FOREIGN KEY ("branch_id") REFERENCES "Branch" ("id");

ALTER TABLE "UserCameraAccess" ADD FOREIGN KEY ("user_id") REFERENCES "AppUser" ("id");

ALTER TABLE "UserCameraAccess" ADD FOREIGN KEY ("camera_id") REFERENCES "Camera" ("id");

ALTER TABLE "Person" ADD FOREIGN KEY ("camera_id") REFERENCES "Camera" ("id");

ALTER TABLE "EnterExit" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Gender" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Age" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "Movement" ADD FOREIGN KEY ("person_id") REFERENCES "Person" ("id");

ALTER TABLE "SecurityLog" ADD FOREIGN KEY ("user_id") REFERENCES "AppUser" ("id");

ALTER TABLE "MaintenanceLog" ADD FOREIGN KEY ("camera_id") REFERENCES "Camera" ("id");

ALTER TABLE "Incident" ADD FOREIGN KEY ("camera_id") REFERENCES "Camera" ("id");

ALTER TABLE "Density" ADD FOREIGN KEY ("camera_id") REFERENCES "Camera" ("id");
