import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    mo.md(
        """
        ![LangChain](img/langchain.jpeg)

        # Runnable Chains avec LangChain

        **LangChain** permet d'enchaîner facilement différents composants de traitement dans un **pipeline unifié**.
        Ces composants — qu'il s'agisse d'un **prompt**, d'un **modèle de langage** ou d'un **outil externe** —
        sont tous traités comme des `Runnable`, c'est-à-dire des **blocs interopérables**.

        Grâce au ***LangChain Expression Language*** (LCEL), nous pouvons chaîner les composants
        via l'opérateur `|` (pipe) et exécuter le tout avec `.invoke()`.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        """
        ![Chains](img/chains.png)

        > **générer un prompt** → **l'envoyer à un LLM** → **interpréter la réponse** → **appeler une API ou fonction**
        """
    )
    return


@app.cell
def __(mo):
    mo.md("# 1. Chargement du modèle LLM local")
    return


@app.cell
def __():
    import os
    from dotenv import load_dotenv
    from langchain_ollama import ChatOllama
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableBranch
    from langchain.prompts import ChatPromptTemplate

    load_dotenv(override=True)
    model = ChatOllama(model="llama3")
    return (
        os, load_dotenv, model, ChatOllama,
        StrOutputParser, RunnableLambda, RunnableParallel, RunnableBranch, ChatPromptTemplate
    )


@app.cell
def __(mo):
    mo.md(
        """
        # 2. Chaîne basique

        Une chaîne simple combine un prompt structuré avec un modèle de langage
        à l'aide de l'opérateur `|`.
        """
    )
    return


@app.cell
def __(model, mo, ChatPromptTemplate):
    # Prompt structuré avec tuples (rôle, message)
    prompt_basic = ChatPromptTemplate.from_messages([
        ("system", "Tu es un expert en mathématiques et un pédagogue dans ce domaine."),
        ("human", "Calcule le double de {value_1}, puis celui de {value_2}")
    ])

    # Chaîne : prompt → model
    chain_basic = prompt_basic | model

    result_basic = chain_basic.invoke({"value_1": 4, "value_2": 2})
    mo.md(result_basic.content)
    return prompt_basic, chain_basic, result_basic


@app.cell
def __(mo):
    mo.md(
        """
        ## Exercice 1

        Créez un prompt qui demande à un modèle de définir un mot donné, dans un style pédagogique.

        1. Utilisez `ChatPromptTemplate.from_messages()` avec un message system et human
        2. Reliez ce prompt à un modèle avec l'opérateur `|`
        3. Testez avec plusieurs disciplines et thèmes
        """
    )
    return


@app.cell
def __(mo):
    # Votre code ici
    mo.md("Complétez l'exercice ci-dessus")
    return


@app.cell
def __(mo):
    mo.md(
        """
        # 3. Chaîne étendue (séquence de runnables)

        L'un des atouts majeurs de LangChain réside dans son système de **chaînes composables**.
        Grâce à l'opérateur `|`, on peut enchaîner autant d'étapes de traitement que voulu.
        """
    )
    return


@app.cell
def __(mo):
    mo.md("### 3.1 Runnable built-in")
    return


@app.cell
def __(model, mo, ChatPromptTemplate, StrOutputParser):
    prompt_extended = ChatPromptTemplate.from_messages([
        ("system", "Tu es un expert en mathématiques et un pédagogue dans ce domaine."),
        ("human", "Calcule le double de {value_1}, puis celui de {value_2}")
    ])

    # Parser qui convertit la sortie en chaîne de caractères
    parser = StrOutputParser()

    # Enchaînement : prompt → model → parser
    chain_extended = prompt_extended | model | parser

    result_extended = chain_extended.invoke({"value_1": 4, "value_2": 2})
    mo.md(result_extended)
    return prompt_extended, parser, chain_extended, result_extended


@app.cell
def __(mo):
    mo.md("### 3.2 Runnable custom")
    return


@app.cell
def __(model, mo, ChatPromptTemplate, StrOutputParser, RunnableLambda):
    prompt_custom = ChatPromptTemplate.from_messages([
        ("system", "Tu es un expert en mathématiques et un pédagogue dans ce domaine."),
        ("human", "Calcule le double de {value_1}, puis celui de {value_2}")
    ])

    parser_custom = StrOutputParser()
    # Runnable custom pour transformer la sortie en majuscules
    uppercase = RunnableLambda(lambda x: x.upper())

    chain_custom = prompt_custom | model | parser_custom | uppercase

    result_custom = chain_custom.invoke({"value_1": 4, "value_2": 2})
    mo.md(result_custom)
    return prompt_custom, parser_custom, uppercase, chain_custom, result_custom


@app.cell
def __(mo):
    mo.md(
        """
        # 4. Chaînes parallèles

        Il est possible d'exécuter plusieurs **chaînes de traitement en parallèle**
        à l'aide du composant `RunnableParallel`.
        """
    )
    return


@app.cell
def __(model, mo, ChatPromptTemplate, StrOutputParser, RunnableParallel):
    system_role = ("system", "Tu es un expert en mathématiques.")

    prompt_add = ChatPromptTemplate.from_messages([
        system_role,
        ("human", "Additionne {value_1} à {value_2}.")
    ])

    prompt_sub = ChatPromptTemplate.from_messages([
        system_role,
        ("human", "Soustrais {value_1} de {value_2}.")
    ])

    chain_add = prompt_add | model | StrOutputParser()
    chain_sub = prompt_sub | model | StrOutputParser()

    # Traitement parallèle
    parallel_chain = RunnableParallel({
        "addition": chain_add,
        "soustraction": chain_sub
    })

    inputs_parallel = {"value_1": 10, "value_2": 4}
    result_parallel = parallel_chain.invoke(inputs_parallel)

    mo.md(f"""
    **Addition :** {result_parallel["addition"]}

    **Soustraction :** {result_parallel["soustraction"]}
    """)
    return (
        system_role, prompt_add, prompt_sub, chain_add, chain_sub,
        parallel_chain, inputs_parallel, result_parallel
    )


@app.cell
def __(mo):
    mo.md(
        """
        ## Exercice 2

        Construisez un mini-analyseur de texte. À partir d'un même paragraphe, vous voulez :
        - Résumer le texte
        - Extraire les mots-clés
        - Détecter la langue
        - Analyser le sentiment

        Utilisez `RunnableParallel` pour exécuter ces 4 analyses en parallèle.
        """
    )
    return


@app.cell
def __(mo):
    # Votre code ici
    mo.md("Complétez l'exercice ci-dessus")
    return


@app.cell
def __(mo):
    mo.md(
        """
        # 5. Branches conditionnelles

        Grâce à `RunnableBranch`, il est possible de router dynamiquement la sortie
        vers différents traitements en fonction de son contenu.
        """
    )
    return


@app.cell
def __(model, mo, ChatPromptTemplate, StrOutputParser, RunnableLambda, RunnableBranch):
    prompt_branch = ChatPromptTemplate.from_messages([
        ("system", "Tu es un expert en mathématiques."),
        ("human", "Calcule le double de {value}. Retourne uniquement le nombre, sans explications.")
    ])

    parser_branch = StrOutputParser()
    base_chain_branch = prompt_branch | model | parser_branch

    # Runnables de traitement
    uppercase_branch = RunnableLambda(
        lambda x: f"Le résultat est {x} (>= 100), transformation en majuscules.".upper()
    )
    lowercase_branch = RunnableLambda(
        lambda x: f"Le résultat est {x} (< 100), tout en minuscules.".lower()
    )

    # Branche selon le contenu généré
    branch = RunnableBranch(
        (lambda x: int(x.strip()) >= 100, uppercase_branch),
        lowercase_branch
    )

    chain_branch = base_chain_branch | branch

    result_branch = chain_branch.invoke({"value": 60})
    mo.md(result_branch)
    return (
        prompt_branch, parser_branch, base_chain_branch,
        uppercase_branch, lowercase_branch, branch, chain_branch, result_branch
    )


@app.cell
def __(mo):
    mo.md(
        """
        ## Exercice 3

        Sur une fiche produit e-commerce, construisez une chaîne qui :

        1. Analyse un commentaire client
        2. Détecte la tonalité (positive, negative, neutral)
        3. Génère une réponse adaptée via `RunnableBranch`

        Exemple : "J'ai bien reçu le produit, mais l'emballage était abîmé."
        → Réponse adaptée au sentiment négatif détecté.
        """
    )
    return


@app.cell
def __(mo):
    # Votre code ici
    mo.md("Complétez l'exercice ci-dessus")
    return


if __name__ == "__main__":
    app.run()
