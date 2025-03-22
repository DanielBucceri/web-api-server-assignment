add error validatio to :

{how to add these erro messages in . Remember im trying to learn not let you do it? 🐾 1. Adopting a Pet (Initial Adoption)
✅ Expected Workflow:
User sends a POST to /adoptions with:
json
Copy
Edit
{
  "user_id": 1,
  "pet_id": 2,
  "adoption_date": "2025-03-20",
  "notes": "First-time adoption"
}
Server:
Verifies the user and pet exist
Checks that pet’s adoption_status is "Available"
Creates a new Adoption record
Adds the user-pet relationship to pet_owners
Updates pet.adoption_status = "Adopted"
⚠️ Edge Cases to Handle:
Pet is already adopted → ❌ Return 400 Bad Request: Pet not available for adoption
User already owns pet → ❌ Return 400 Bad Request: User already owns this pet}

