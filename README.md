# PastAI

PastAI is an AI-powered language-learning and memory-assist application designed for university students and individuals with memory challenges. The application allows users to record daily voice journals in Turkish or English, which are processed to enable personalized, context-aware conversations and reminders.

## Features

- **Voice Journaling**: Users can record their thoughts and experiences in their preferred language.
- **AI-Driven Conversations**: The application utilizes AI to provide personalized responses based on user input.
- **Memory Assistance**: Users receive reminders and context-aware prompts to help with memory retention.
- **User-Friendly Interface**: Built with Next.js for a seamless user experience.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Node.js 14 or higher
- PostgreSQL or Redis for context storage

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pastai.git
   cd pastai
   ```

2. Set up the backend:
   - Navigate to the backend directory:
     ```
     cd backend/app
     ```
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the frontend directory:
     ```
     cd ../frontend
     ```
   - Install the required Node.js packages:
     ```
     npm install
     ```

### Running the Application

1. Start the backend server:
   ```
   cd backend/app
   uvicorn main:app --reload
   ```

2. Start the frontend development server:
   ```
   cd frontend
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:3000` to access the application.

## API Endpoints

- **POST /api/v1/journal**: Record a journal entry.
- **GET /api/v1/context**: Retrieve user context.
- **POST /api/v1/chat**: Send input and receive a response.
- **GET /api/v1/reminders**: List reminders.
- **POST /api/v1/reminders**: Create a reminder.

## Testing

To run the tests for the backend API, navigate to the `backend/tests` directory and run:
```
pytest test_api.py
```

## Legal & Privacy

PastAI is compliant with GDPR and KVKK regulations. User data is stored securely, and explicit consent is required for any data processing.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.