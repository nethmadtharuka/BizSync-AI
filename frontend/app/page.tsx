export default async function Home() {
  const res = await fetch("http://localhost:8080/api/health", { cache: "no-store" });
  const data = await res.json();

  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold">BizSync AI Dashboard</h1>
      <p className="mt-2">Local dev running ✅</p>
      <pre className="mt-4 rounded bg-gray-100 p-4 text-sm">
        {JSON.stringify(data, null, 2)}
      </pre>
    </main>
  );
}
