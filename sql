-- Add Departments
INSERT INTO main_department (name, description) VALUES
('IT', 'Information Technology Department'),
('Business', 'Business & Management Department');

-- Add Subjects for IT
INSERT INTO main_subject (name, department_id) VALUES
('Web Development', (SELECT id FROM main_department WHERE name='IT')),
('Python Programming', (SELECT id FROM main_department WHERE name='IT')),
('Networking', (SELECT id FROM main_department WHERE name='IT'));

-- Add Subjects for Business
INSERT INTO main_subject (name, department_id) VALUES
('Accounting', (SELECT id FROM main_department WHERE name='Business')),
('Finance', (SELECT id FROM main_department WHERE name='Business')),
('Marketing', (SELECT id FROM main_department WHERE name='Business'));
ALTER TABLE main_admissionapplication ADD COLUMN department_id integer;
ALTER TABLE main_admissionapplication ADD COLUMN subject_id integer;

-- Optional: add foreign key constraints
ALTER TABLE main_admissionapplication
    ADD CONSTRAINT admissionapplication_department_fk FOREIGN KEY (department_id)
    REFERENCES main_department(id);

ALTER TABLE main_admissionapplication
    ADD CONSTRAINT admissionapplication_subject_fk FOREIGN KEY (subject_id)
    REFERENCES main_subject(id);
