// src/components/Content.js
import React from 'react';
import Graph from '../Graph/Graph';
import NewsFeed from '../NewsFeed/newsfeed'

// import styles
import './Content.css';

const Content = (props) => {
  const graphType = 'sentiment';
  return (
      <div className="content">
        <h1>Financials Graph</h1>
        <div className="data-insights">
          <Graph value={graphType}/> 
          <NewsFeed value = "newsfeed"/>  
        
        </div>
        <div className="text-wrapper">          
            <p>Based on the graphed data above, we recommend purchasing on dates where public sentiment changes from negative to positive.</p>
          </div>
        
      </div>
    );
};

export default Content;