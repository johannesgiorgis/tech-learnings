# Introduction to Alembic

Getting started on [Alembic Tutorial].

## Getting started

```bash
# install alembic
(env) > pip install alembic
... installed alembic 1.4.0, ....

# initialiaze alembic folder at folder above package!
# This will create the alembic folder and the alembic.ini configuration file
(env) ❯ alembic init alembic
  Creating directory ./alembic ...  done
  Creating directory ./alembic/versions ...  done
  Generating ./alembic.ini ...  done
  Generating ./alembic/script.py.mako ...  done
  Generating ./alembic/env.py ...  done
  Generating ./alembic/README ...  done
  Please edit configuration/connection/logging settings in './alembic.ini' before proceeding.

# alembic folder location:
❯ tree -L 1 .
.
├── alembic
├── alembic.ini
├── chapter07_bootstrap
├── data
├── Pipfile
├── Pipfile.lock
├── pypi_org
└── README.md

4 directories, 4 files

```

## Configuring Alembic

```bash
# alembic.ini

# lots of optional settings ...

sqlalchemy.url = sqlite:///./pypi_web/db/pypi_dev.sqlite
```


## Making a Change

You can make changes using Alembic via two ways:

- Manual changes
- SQLAlchemy-based changes

### Manual Changes

Let's explore the manual changes approach first:

```bash
# record a revision with a message
(env) $ alembic revision -m "add keywords column"
  Generating ./alembic/versions/68d7282c8600_add_keywords_column.py ...  done
```

```python
# 68d7282c8600_add_keywords_column.py

# revision identifiers, used by Alembic.
revision = '68d7282c8600'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass

# -> Need to define the changes to upgrade and downgrade to/from this version.

# e.g.


def upgrade():
    op.add_column('packages', sa.Column('keywords', sa.String, nullable=True))


def downgrade():
    op.drop_column('packages', sa.Column('keywords'))
```

This migration is pretty straightforward but can be a bit tricky. We may want to double check that this column does not exist before you try to add it. If it does, this migration would fail and everything that depends upon it will subsequently fail as well and that won't be great - the same issue will occur for dropping the table as well.

The safer approach is to use Alembic helpers:

```python
# IMPORTANT: Name: alembic_helpers.py, please in alembic folder.

from alembic import op
from sqlalchemy import engine_from_config
from sqlalchemy.engine import reflection


def table_has_column(table, column):
    config = op.get_context().config
    engine = engine_from_config(
        config.get_section(config.config_ini_section), prefix='sqlalchemy.'
    )
    insp = reflection.Inspector.from_engine(engine)
    has_column = False

    for col in insp.get_columns(table):
        if column not in col['name']:
            continue
        has_column = True
    return has_column

```

And the way to utilize it is:

```python
# 68d7282c8600_add_keywords_column.py

# revision identifiers, used by Alembic.

import imp
import os

alembic_helpers = imp.load_package('alembic_helpers', os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alembic_helpers.py')))

def upgrade():
	if not alembic_helpers.table_has_column('packages', 'keywords'):
    	op.add_column('packages', sa.Column('keywords', sa.String, nullable=True))

```


Ask alembic what version are we on?

```bash
(env) ❯ alembic current
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.

# This means there is no version set in your DB.
```

Upgrade the DB:

```bash
(env) ❯ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 8905feea7a37 -> 68d7282c8600, add keywords column
```

Ask alembic what version are we on?


```bash
(env) ❯ alembic current
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
68d7282c8600 (head)
```

This version is stored in the database under the `alembic_version` table.

### SQLAlchemy-based changes

Let's explore the SQLAlchemy based changes:

To allow for auto-generated changes:

```python
# env.py

import pypi_web
# Ensure SqlAlchemyBase sees all your various models
from pypi_web.data import *

target_metadata = pypi_web.data.modelbase.SqlAlchemyBase.metadata
```

Now to make to a change, modify the necessary SQLAlchemy code in your application. Then:

```bash
# record a revision with a message
(env) $ alembic revision --autogenerate -m "add last login column"
  Detected added column 'users.last_login'
  Generating ./alembic/versions/e7d7282c7435_add_last_login_column.py ...  done
```

The automatically generated migration script is below:

```python
# e7d7282c7435_add_last_login_column.py

revision identifiers, used by Alembic.
revision = 'e7d7282c7435'
down_revision = '6898ef996d1c'
branch_levels = None
depends_on = None

def upgrade():
	# ### commands auto generated by Alembic - please adjust! ###
	op.add_column('users', sa.Column('last_login', sa.String, nullable=True))
	# ### end Alembic commands ###
```

To upgrade the database:

```bash
(env) ❯ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 6898ef996d1c -> e7d7282c7435, add last login column
```

[Alembic Tutorial]: https://alembic.zzzcomputing.com/en/latest/tutorial.html