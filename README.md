![LangChain](img/langchain.jpeg)

Ce projet propose une introduction pédagogique à l'utilisation
des **chaînes exécutables (Runnable Chains)** de **LangChain**,
permettant de structurer des flux de traitement modulaires et réutilisables avec des LLMs.
Il est conçu pour comprendre comment composer des étapes de traitement en chaînes exécutables.

## Objectifs pédagogiques

- Comprendre le concept de chaîne exécutable (Runnable Chain) dans LangChain  
- Apprendre à composer des étapes de traitement modulaires  
- Explorer la création de pipelines personnalisés pour le traitement de données avec des LLMs  
- Fournir une base pour le développement d'applications complexes utilisant LangChain  

## Prérequis

- Python ≥ 3.10  
- Environnement Jupyter (ou autre IDE compatible)  
- Clé API OpenAI (ou autre LLM compatible)  

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/maxime-lenne/course-langchain-runnable-chain
   cd runnable-chain
   ```

2. Créez un environnement virtuel (optionnel mais recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Lancez le notebook :

   ```bash
   jupyter notebook
   ```

## Structure du projet

- `langchain.ipynb` : notebook principal illustrant l'utilisation des chaînes exécutables de LangChain  
- `img/` : ressources visuelles pour la présentation  
- `requirements.txt` : liste des dépendances Python nécessaires  
