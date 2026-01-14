# LangGraph Playlist

This repository contains mini projects designed to build understanding of **LangGraph** - a framework for building stateful, multi-actor applications with language models.

## Projects Overview

### 1. **Lecture 1: BMI Calculator - Basic State Graph**
   - **Concept**: Introduction to LangGraph fundamentals
   - **Features**:
     - Create a `BMIState` TypedDict with height, weight, and bmi fields
     - Implement `compute_bmi()` function to calculate BMI from height and weight
     - Build a StateGraph with nodes and edges (START → calculate_bmi → END)
   - **Key Learnings**: Basic node creation, state management, graph structure

### 2. **Lecture 2: BMI Calculator with Categorization - Conditional Routing**
   - **Concept**: Extending the BMI calculator with conditional logic
   - **Features**:
     - Extended `BMIState` with a category field
     - Implement `label_bmi()` function to categorize BMI values:
       - Underweight (BMI < 18.5)
       - Normal weight (18.5 ≤ BMI < 24.9)
       - Overweight (25 ≤ BMI < 29.9)
       - Obese (BMI ≥ 30)
     - Connect compute_bmi → label_bmi → END
   - **Key Learnings**: Multi-step workflows, state transformation, sequential node execution

### 3. **Lecture 3: LLM Question-Answering Bot - LangChain Integration**
   - **Concept**: Integrating ChatGroq (Groq API) with LangGraph
   - **Features**:
     - Load API keys using `dotenv` library
     - Create `LLMState` with question and answer fields
     - Implement `llm_qa()` function using ChatGroq (llama-3.1-8b-instant model)
     - Build a Q&A bot that answers user questions using LLM
   - **Key Learnings**: LLM integration, environment variable management, API key handling

### 4. **Lecture 4: Blog Generator - Multi-Stage LLM Workflow**
   - **Concept**: Building a complex workflow with multiple LLM calls
   - **Features**:
     - Create `BlogState` with Title, Outline, and Blog fields
     - Implement multi-stage workflow:
       1. Generate outline from title
       2. Generate full blog content from outline
     - Use Groq API (mixtral-8x7b-32768 model) for content generation
     - Display workflow graph with visualization
   - **Key Learnings**: Complex workflows, multi-stage LLM chains, graph visualization

### 5. **Lecture 5: Quadratic Equation Solver - Branching Logic**
   - **Concept**: Using conditional branching in LangGraph
   - **Features**:
     - Create `QuadraticEquation` state with coefficients (a, b, c) and results
     - Implement `discriminant()` function to calculate the discriminant (b² - 4ac)
     - Branching logic based on discriminant value:
       - If discriminant > 0: Two real roots
       - If discriminant = 0: One real root
       - If discriminant < 0: Complex roots
     - Complete root calculation and result formatting
   - **Key Learnings**: Conditional routing, mathematical operations, state branching

### 6. **Lecture 6: Tweet Generator with Iterative Refinement - Agentic Loop**
   - **Concept**: Building an agentic workflow with feedback loops and iterations
   - **Features**:
     - Create `TweetState` with topic, tweet, evaluation, feedback, and history tracking
     - Use `Annotated` with operator.add for list accumulation (tweet_history, feedback_history)
     - Implement `generate_tweet()` function with creative prompting for humor and originality
     - Implement `evaluate_tweet()` function to review generated tweets
     - Implement `refine_tweet()` function for iterative improvements
     - Conditional routing: approved tweets → END, needs improvement → regenerate
     - Track iterations with max_iteration limit to prevent infinite loops
   - **Key Learnings**: Agentic loops, state accumulation, iterative refinement, conditional routing

### 7. **Lecture 7: Structured Output with Pydantic - Type-Safe LLM Responses**
   - **Concept**: Ensuring LLM returns structured, machine-readable data
   - **Features**:
     - Use Pydantic BaseModel for defining expected LLM output structure
     - Implement structured output parsing to avoid:
       - Invalid JSON formatting
       - Missing keys in responses
       - Extra text around JSON
       - Escaping issues (double curly braces)
     - Integrate with Groq API for reliable structured responses
   - **Key Learnings**: Pydantic models, structured outputs, JSON validation, schema definition

### 8. **Lecture 8: Cricket Statistics Calculator - Advanced State Management**
   - **Concept**: Complex state management with multiple calculations and tracking
   - **Features**:
     - Create `Cricket` state with match statistics (runs, balls, fours, sixes, etc.)
     - Calculate Strike Rate (SR) = (runs/balls) × 100
     - Calculate Boundary By Boundary (BRB) metrics
     - Generate match summary with analysis
     - Implement multiple interconnected calculation nodes
     - State persistence and checkpointing with InMemorySaver
   - **Key Learnings**: Complex state calculations, multiple transformations, state persistence

### 9. **LangGraph Base: Basic Graph Structure**
   - **Concept**: Foundational concepts of LangGraph
   - **Features**:
     - Simple graph structure demonstration
     - Node and edge connections
     - Graph compilation and execution
     - State management basics
   - **Key Learnings**: Graph fundamentals, node execution, state flow

## Key Technologies & Libraries

- **LangGraph**: Graph-based state management framework
- **LangChain**: Framework for building LLM applications
- **Groq API**: Fast LLM inference (models: llama-3.1-8b-instant, mixtral-8x7b-32768)
- **Pydantic**: Data validation and structured data models
- **Python TypedDict**: Type-safe state definitions
- **dotenv**: Environment variable management

## Common Patterns Used

1. **TypedDict States**: Define graph state structure
2. **Node Functions**: Process and transform state
3. **State Graph Builder**: Construct graph with add_node() and add_edge()
4. **Conditional Routing**: Branch execution based on state
5. **Agentic Loops**: Iterative refinement with feedback
6. **Structured Outputs**: Pydantic models for LLM validation
7. **Graph Visualization**: IPython display for workflow diagrams
8. **Checkpointing**: InMemorySaver for state persistence

## Setup Requirements

- Python 3.8+
- Required packages: `langgraph`, `langchain`, `langchain-groq`, `pydantic`, `python-dotenv`
- Groq API key (set in `.env` file as `GROQ_API_KEY`)

## Usage

Each Jupyter notebook can be run independently. Set up your `.env` file with:
```
GROQ_API_KEY=your_api_key_here
```

Then run the cells in each notebook to see LangGraph workflows in action.
