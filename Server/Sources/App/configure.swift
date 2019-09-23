import FluentSQLite
import Vapor
import PostgreSQL

/// Called before your application initializes.
public func configure(_ config: inout Config, _ env: inout Environment, _ services: inout Services) throws {
    // Register providers first
    try services.register(FluentSQLiteProvider())
    try services.register(PostgreSQLProvider())

    // Register routes to the router
    let router = EngineRouter.default()
    try routes(router)
    services.register(router, as: Router.self)

    // Register middleware
    var middlewares = MiddlewareConfig() // Create _empty_ middleware config
    // middlewares.use(FileMiddleware.self) // Serves files from `Public/` directory
    middlewares.use(ErrorMiddleware.self) // Catches errors and converts to HTTP response
    services.register(middlewares)

    // Configure a SQLite database
    let sqlite = try SQLiteDatabase(storage: .memory)
    
    // Configure a PostgreSQL database
    let postgresql = PostgreSQLDatabase(config: PostgreSQLDatabaseConfig(hostname: "localhost", port: 5432, username: "postgres", database: "postgres"))
    
    // Registers a list of databases
    var databases = DatabasesConfig()
    
    // Register the configured SQLite database to the database config.
    databases.add(database: sqlite, as: .sqlite)
    services.register(databases)
    
    // Register the configured PostgreSQL database to the database config.
    databases.add(database: postgresql, as: .psql)
    services.register(databases)

    // Configure migrations
    var migrations = MigrationConfig()
    migrations.add(model: Todo.self, database: .sqlite)
    services.register(migrations)
}
