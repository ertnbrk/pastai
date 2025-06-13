import React from 'react';
import Header from '../components/Header';

const Home: React.FC = () => {
    return (
        <div>
            <Header />
            <main>
                <h1>Welcome to PastAI</h1>
                <p>Your AI-powered language-learning and memory-assist application.</p>
            </main>
        </div>
    );
};

export default Home;