# Configuración de Supabase

1. Crea la tabla con el SQL de `schema.sql` en el SQL Editor de Supabase.
2. Abre `index.html` para agregar productos.
3. Abre `catalogo.html` para ver los productos que se guardan.

Nota importante: la versión online ahora usa una sesión anónima de Supabase desde el navegador, que es la forma correcta y segura para un catálogo público. Si quieres una versión aún más estricta, puedes añadir políticas RLS más específicas para `insert`, `update` y `delete`.
