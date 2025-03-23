```markdown
# Pet Adoption API

This is a simple Flask based web server for a pet adoption management system. It handles Users, Pets, Addresses, and Adoption records. Each resource supports various CRUD operations, and a Postgres database is used for persistent storage.

---

## Project Overview

**Goal**: Provide a basic web API where:

- Users can be created, updated, and deleted.
- Pets can be listed, created, updated, deleted, and released from owners.
- Addresses can be added and linked to users.
- Adoptions can be tracked, ensuring pets are only adopted once.

**Tech Used**:
- Flask (for the web server)
- Flask SQLAlchemy (ORM for database access)
- Marshmallow (for data validation & serialization)
- PostgreSQL (recommended for the DB, but interchangeable if you change the `DB_URI`)

---

## Getting Started

1. **Clone or Download this repository.**

2. **Create a Virtual Environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies using the provided `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your Database:**
   - Create a Postgres database.
   - Copy its connection string into an environment variable named `DB_URI`. Example:
     ```bash
     export DB_URI='postgresql://user:password@localhost:<port>/my_database'
     ```
   - Or set it in a `.env` file if you prefer.

---

## Running the App Locally

1. **Initialize the Database (drop and create tables, then seed some data):**
   ```bash
   flask db init
   flask db seed
   ```

2. **Start the Server:**
   ```bash
   python main.py
   ```

   The server should default to `http://127.0.0.1:5000`.

---

## Endpoints (Quick Overview)

### Users
- `GET /users` – List all users  
- `POST /users` – Create a new user  
- `GET /users/<user_id>` – Get a single user by ID  
- `PATCH /users/<user_id>` – Update a user (partial or full)  
- `DELETE /users/<user_id>` – Delete a user  

### Pets
- `GET /pets` – List all pets  
- `POST /pets` – Create a new pet  
- `GET /pets/<pet_id>` – Get a single pet by ID  
- `PATCH /pets/<pet_id>` – Update a pet  
- `DELETE /pets/<pet_id>` – Delete a pet  
- `POST /pets/<pet_id>/release` – Release an adopted pet back to “available”  

### Addresses
- `GET /addresses` – List all addresses  
- `POST /addresses` – Create a new address  
- `GET /addresses/<address_id>` – Get a single address  
- `PATCH /addresses/<address_id>` – Update an address  
- `DELETE /addresses/<address_id>` – Delete an address  

### Adoptions
- `GET /adoptions` – List all adoptions  
- `POST /adoptions` – Create a new adoption record  
- `GET /adoptions/<adoption_id>` – Get an adoption record by ID  

(No update or delete for adoption records to maintain history.)

---

## Deployment

- Ensure your environment variables (like `DB_URI`) are set on your hosting service (Heroku, Render, Railway, etc.).
- Once deployed, the same routes above should be available at your public URL.

---

## Future Improvements

- **Authentication & Authorization** – Require users to log in before adopting a pet.
- **Better Data Validations**
- **More Detailed Pet Info** 
