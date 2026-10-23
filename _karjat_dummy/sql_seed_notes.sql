-- Karjat dummy data notes
-- Prefer API create (property_create_body.json) over raw SQL.
-- Raw inserts skip workflow/idgen/user creation and often break the UI.

-- After a successful API create, verify with:
-- SELECT propertyid, tenantid, status, oldpropertyid
-- FROM eg_pt_property
-- WHERE tenantid = 'mh.karjatmunicipalcouncil'
--    OR oldpropertyid = 'KJT-DUMMY-0001';

-- Cleanup later:
-- (delete via property service / controlled SQL only after confirming IDs)
