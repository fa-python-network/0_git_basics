import Vapor


struct PostgreSQLVersion: Codable {
    let version: String
}


/// Register your application's routes here.
public func routes(_ router: Router) throws {
    
    // The home page shows the PostgreSQL version
    router.get { req in
        return req.withPooledConnection(to: .psql) { conn in
            return conn.raw("SELECT version()").all(decoding: PostgreSQLVersion.self)
        }.map { rows in
            return rows[0].version
        }
    }
    
}
