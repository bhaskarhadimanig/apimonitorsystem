import { Table, TableHead, TableRow, TableCell, TableBody } from "@mui/material";
export default function EmailGroupTable({ groups }) {
  return (
    <Table>
      <TableHead>
        <TableRow>
          <TableCell>Group Name</TableCell>
          <TableCell>Emails</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {groups.map((group: any) => (
          <TableRow key={group.id}>
            <TableCell>{group.name}</TableCell>
            <TableCell>{group.emails.map((e: any) => e.email).join(", ")}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}