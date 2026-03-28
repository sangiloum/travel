# travel.dimag.kr

## Updating bus schedules

Run the following script to fetch the latest departure times from the bustago.or.kr API and regenerate the YAML files in `_data/schedules/`:

```bash
pip install requests pyyaml   # first time only
python scripts/update_schedules.py
```

The script updates all five routes (`icn-govcomplex`, `icn2-govcomplex`, `icn-doryong`, `icn2-doryong`, `cjj-yuseong`) and writes `first_bus`, `last_bus`, and fare/time data into each file. The route pages pick up the new values automatically on the next Jekyll build.
