import React, { useState } from 'react';
import Preferences from './Preferences';
import Personalization from './Personalization';
import Privacy from './Privacy';
import DataManagement from './DataManagement';
import Helpsettings from './Helpsettings';
import './Settings.css';

const Settings = () => {
  const [activeTab, setActiveTab] = useState('preferences');
  const [darkMode, setDarkMode] = useState(false);

  const handleTabChange = (tab) => setActiveTab(tab);
  const toggleDarkMode = () => setDarkMode(!darkMode);

  return (
    <div className={`tab-container ${darkMode ? 'dark-mode' : ''}`}>
      <div className="tab-navigation">
        <button
          className={`tab-button ${activeTab === 'preferences' ? 'active' : ''}`}
          onClick={() => handleTabChange('preferences')}
        >
          Preferences
        </button>
        <button
          className={`tab-button ${activeTab === 'personalization' ? 'active' : ''}`}
          onClick={() => handleTabChange('personalization')}
        >
          Personalization
        </button>
        <button
          className={`tab-button ${activeTab === 'privacy' ? 'active' : ''}`}
          onClick={() => handleTabChange('privacy')}
        >
          Privacy
        </button>
        <button
          className={`tab-button ${activeTab === 'data-management' ? 'active' : ''}`}
          onClick={() => handleTabChange('data-management')}
        >
          Data Management
        </button>
        <button
          className={`tab-button ${activeTab === 'helpsettings' ? 'active' : ''}`}
          onClick={() => handleTabChange('helpsettings')}
        >
          Help
        </button>
      </div>

      <div className="tab-content">
        {activeTab === 'preferences' && <Preferences toggleDarkMode={toggleDarkMode} />}
        {activeTab === 'personalization' && <Personalization />}
        {activeTab === 'privacy' && <Privacy />}
        {activeTab === 'data-management' && <DataManagement />}
        {activeTab === 'helpsettings' && <Helpsettings />}
      </div>
    </div>
  );
};

export default Settings;
