grant select, insert, update, delete on table public.products to anon;
grant select, insert, update, delete on table public.products to authenticated;
grant select, insert, update, delete on table public.products to service_role;
grant usage, select, update on sequence public.products_id_seq to anon;
grant usage, select, update on sequence public.products_id_seq to authenticated;
grant usage, select, update on sequence public.products_id_seq to service_role;
