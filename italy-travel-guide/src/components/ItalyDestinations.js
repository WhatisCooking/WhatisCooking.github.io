import React, { useState } from 'react';
import './ItalyDestinations.css';

const ItalyDestinations = () => {
  const [selectedDestination, setSelectedDestination] = useState(null);

  const destinations = [
    {
      id: 1,
      name: 'Rome',
      region: 'Lazio',
      image: 'https://images.unsplash.com/photo-1515542622106-78bda8ba0e5b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
      description: 'The Eternal City, home to the Colosseum, Vatican City, and centuries of history.',
      highlights: ['Colosseum', 'Vatican Museums', 'Trevi Fountain', 'Roman Forum'],
      bestTime: 'April-June, September-October'
    },
    {
      id: 2,
      name: 'Venice',
      region: 'Veneto',
      image: 'https://images.unsplash.com/photo-1514890547357-a9ee288728e0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
      description: 'A unique city built on water, famous for its canals, gondolas, and stunning architecture.',
      highlights: ['St. Mark\'s Square', 'Doge\'s Palace', 'Grand Canal', 'Rialto Bridge'],
      bestTime: 'April-June, September-November'
    },
    {
      id: 3,
      name: 'Florence',
      region: 'Tuscany',
      image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
      description: 'The birthplace of the Renaissance, filled with art, culture, and architectural masterpieces.',
      highlights: ['Uffizi Gallery', 'Duomo', 'Ponte Vecchio', 'Michelangelo\'s David'],
      bestTime: 'April-June, September-October'
    },
    {
      id: 4,
      name: 'Milan',
      region: 'Lombardy',
      image: 'https://images.unsplash.com/photo-1513581166391-887928dc2fc5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
      description: 'Italy\'s fashion and design capital, known for luxury shopping and modern architecture.',
      highlights: ['Duomo di Milano', 'La Scala', 'Navigli District', 'Quadrilatero della Moda'],
      bestTime: 'April-June, September-November'
    },
    {
      id: 5,
      name: 'Amalfi Coast',
      region: 'Campania',
      image: 'https://images.unsplash.com/photo-1534445967719-8474f9f35570?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
      description: 'Stunning coastal scenery with dramatic cliffs, colorful villages, and crystal-clear waters.',
      highlights: ['Positano', 'Amalfi', 'Ravello', 'Capri Island'],
      bestTime: 'April-June, September-October'
    },
    {
      id: 6,
      name: 'Tuscany',
      region: 'Tuscany',
      image: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
      description: 'Rolling hills, vineyards, medieval towns, and world-class wine and cuisine.',
      highlights: ['Siena', 'Pisa', 'Chianti Wine Region', 'Val d\'Orcia'],
      bestTime: 'April-June, September-October'
    },
    {
      id: 7,
      name: 'Cinque Terre',
      region: 'Liguria',
      image: 'https://images.unsplash.com/photo-1516483638261-f4dbaf036963?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2072&q=80',
      description: 'Five picturesque fishing villages perched on rugged coastal cliffs.',
      highlights: ['Monterosso', 'Vernazza', 'Corniglia', 'Manarola', 'Riomaggiore'],
      bestTime: 'April-June, September-October'
    },
    {
      id: 8,
      name: 'Sicily',
      region: 'Sicily',
      image: 'https://images.unsplash.com/photo-1555992336-fb0d29498b13?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
      description: 'Italy\'s largest island with ancient Greek temples, active volcanoes, and diverse culture.',
      highlights: ['Mount Etna', 'Palermo', 'Taormina', 'Valley of Temples'],
      bestTime: 'April-June, September-November'
    }
  ];

  const handleDestinationClick = (destination) => {
    setSelectedDestination(selectedDestination?.id === destination.id ? null : destination);
  };

  return (
    <div className="italy-destinations">
      <header className="header">
        <h1 className="main-title">Discover Italy</h1>
        <p className="subtitle">Explore the most beautiful destinations in the boot-shaped peninsula</p>
      </header>

      <div className="destinations-grid">
        {destinations.map((destination) => (
          <div
            key={destination.id}
            className={`destination-card ${selectedDestination?.id === destination.id ? 'active' : ''}`}
            onClick={() => handleDestinationClick(destination)}
          >
            <div className="image-container">
              <img src={destination.image} alt={destination.name} className="destination-image" />
              <div className="overlay">
                <h3 className="destination-name">{destination.name}</h3>
                <p className="destination-region">{destination.region}</p>
              </div>
            </div>
            
            {selectedDestination?.id === destination.id && (
              <div className="destination-details">
                <p className="description">{destination.description}</p>
                <div className="highlights">
                  <h4>Must-See Attractions:</h4>
                  <ul>
                    {destination.highlights.map((highlight, index) => (
                      <li key={index}>{highlight}</li>
                    ))}
                  </ul>
                </div>
                <div className="best-time">
                  <strong>Best Time to Visit:</strong> {destination.bestTime}
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      <footer className="footer">
        <p>🇮🇹 Experience the magic of Italy - where every corner tells a story</p>
      </footer>
    </div>
  );
};

export default ItalyDestinations;