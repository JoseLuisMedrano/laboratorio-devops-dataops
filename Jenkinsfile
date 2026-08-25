pipeline { 
agent any 
stages { 
stage('Validar Python') { 
steps { 
bat 'python --version' 
} 
 
        } 
 
        stage('Instalar dependencias') { 
 
            steps { 
                bat 'pip install pandas' 
                bat 'pip install psycopg2-binary' 
            } 
 
        } 
 
        stage('Ejecutar procesamiento') { 
 
            steps { 
                bat 'python scripts/procesamiento.py' 
            } 
 
        } 
 
        stage('Validación final') { 
 
            steps { 
                echo 'Pipeline ejecutado correctamente' 
            } 
 
        } 
 
    } 
 
}