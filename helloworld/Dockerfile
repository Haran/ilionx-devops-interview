FROM eclipse-temurin:21.0.2_13-jdk-jammy

# Tomcat port
EXPOSE 8080

# Copy to dedicated directory (dedicated user is not listed in requirements)
WORKDIR /app
COPY build/libs/helloworld.jar /app/helloworld.jar

# Must have for all containers
HEALTHCHECK --interval=10s --timeout=5s CMD curl -f http://localhost:8080 || exit 1

# Default entrypoint
ENTRYPOINT ["java", "-jar", "/app/helloworld.jar"]
